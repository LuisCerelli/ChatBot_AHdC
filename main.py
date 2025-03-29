from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
import requests
import threading
import time

# Obtener token desde Hugging Face Secrets
HF_TOKEN = os.environ.get("HF_TOKEN")

# Verificación al arrancar
assert HF_TOKEN is not None, "❌ HF_TOKEN no fue cargado correctamente"
print("✅ FastAPI cargado. Token presente:", bool(HF_TOKEN))

# Inicializar app
app = FastAPI()

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Modelo de entrada
class ChatRequest(BaseModel):
    message: str

@app.get("/")
def root():
    return {"message": "✅ Backend FastAPI operativo"}

# Endpoint del chatbot
@app.post("/chat")
async def chat_endpoint(chat: ChatRequest):
    headers = {"Authorization": f"Bearer {HF_TOKEN}"}
    payload = {
        "inputs": f"Responde en español: {chat.message}",
        "parameters": {
            "max_new_tokens": 150,
            "temperature": 0.7
        }
    }

    try:
        response = requests.post(
            "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.1",
            headers=headers,
            json=payload,
            timeout=20  # ⏰ importante para evitar cuelgues
        )

        if response.status_code == 200:
            output = response.json()
            if isinstance(output, list) and "generated_text" in output[0]:
                bot_reply = output[0]["generated_text"]
            elif "generated_text" in output:
                bot_reply = output["generated_text"]
            else:
                bot_reply = "🤖 No se encontró respuesta válida."
        else:
            bot_reply = f"⚠️ Error {response.status_code}: {response.text}"

        return {"response": bot_reply}

    except requests.exceptions.RequestException as req_error:
        print("❌ Error en la llamada al modelo HF:", req_error)
        return {"response": "🚫 Error al contactar el modelo de Hugging Face."}
    except Exception as e:
        print("❌ Error inesperado:", e)
        return {"response": f"⚠️ Error inesperado: {str(e)}"}

# Hilo para mantener activo el backend
def keep_alive():
    while True:
        time.sleep(60)

threading.Thread(target=keep_alive, daemon=True).start()
