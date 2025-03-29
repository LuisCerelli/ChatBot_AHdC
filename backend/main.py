# backend/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv
import os
import requests

# Cargar token desde .env
load_dotenv()
HF_TOKEN = os.getenv("HF_TOKEN")

# Inicializar app
app = FastAPI()

# CORS: permitir frontend externo
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Podés restringir a tu dominio si querés
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


# Endpoint principal
@app.post("/chat")
async def chat_endpoint(chat: ChatRequest):
    try:
        headers = {"Authorization": f"Bearer {HF_TOKEN}"}
        payload = {
            "inputs": f"Responde en español:{chat.message}",
            "parameters": {
                "max_new_tokens": 150,
                "temperature": 0.7
            }
        }

        response = requests.post(
            "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.1",
            headers=headers,
            json=payload
        )

        if response.status_code == 200:
            output = response.json()
            # El modelo puede devolver distintas formas, cubrimos ambas
            if isinstance(output, list) and "generated_text" in output[0]:
                bot_reply = output[0]["generated_text"]
            elif "generated_text" in output:
                bot_reply = output["generated_text"]
            else:
                bot_reply = "🤖 No se encontró respuesta válida."
        else:
            bot_reply = f"⚠️ Error {response.status_code}: {response.text}"

        return {"response": bot_reply}

    except Exception as e:
        return {"error": str(e)}
