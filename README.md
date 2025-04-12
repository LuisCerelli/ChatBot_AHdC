# 📄 — *Chatbot Huella de Carbono* 🌱🤖
<p align="center">
  <img scr="paginareal/chatbot/Imagenes-logos/Muestra_Chatbot_Real.gif" alt="Demo Chatbot" width="480"/>
</p>

## 🧠 Chatbot Interactivo - Asociación Huella de Carbono 🌍

Este proyecto implementa un chatbot inteligente para la página web de la Asociación Huella de Carbono, diseñado para ofrecer respuestas automáticas en temas de sostenibilidad, huella de carbono y medio ambiente, usando inteligencia artificial.

## 📌 ¿Qué hace este chatbot?

- Escucha preguntas del usuario en un widget web flotante y elegante.
- Se comunica con un modelo de lenguaje grande (LLM) alojado en Hugging Face Spaces.
- Devuelve respuestas en español, de forma clara y educativa.
- Se puede personalizar fácilmente con nuevas preguntas rápidas, colores, íconos o estilo.

---

## 🧱 Estructura del proyecto

```bash
pagina_real/
│
├── huella_local.html                 # Página HTML principal con el chatbot embebido
├── chatbot/
│   ├── chatbot.js                    # Lógica del comportamiento del chatbot (frontend)
│   ├── styles.css                    # Estilos visuales personalizados (burbuja, chat, colores)
│   └── Imagenes-logos/              # Iconos y avatares usados
│
├── huella_local_files/              # Archivos estáticos copiados del sitio original
```

---

## 💻 Cómo funciona

1. El usuario accede a `huella_local.html`.
2. Se muestra una **burbuja flotante de bienvenida**.
3. Al hacer clic, se abre la ventana del chatbot.
4. Los mensajes se envían al backend alojado en **Hugging Face Spaces**.
5. El modelo responde con una respuesta generada en lenguaje natural.
6. El mensaje se muestra en pantalla.

---

## 🌐 Backend en Hugging Face Spaces

El backend fue creado en un **Space nuevo y funcional**, utilizando `FastAPI`, alojado con Docker, y conectado al modelo:

```
mistralai/Mistral-7B-Instruct-v0.1
```

### 🔗 Endpoint real del chatbot:

```
https://luisdsai-chatbot-huella-backend-v2.hf.space/chat
```

---

## ⚙️ Cómo se construyó el backend

Archivos clave subidos a Hugging Face:

### `main.py`

Contiene el servidor FastAPI, el endpoint `/chat`, y la conexión al modelo de Hugging Face. Incluye validaciones, `timeout`, y un hilo para evitar que el Space se apague automáticamente.

### `Dockerfile`

```dockerfile
FROM python:3.11

RUN useradd -m -u 1000 user
USER user
ENV PATH="/home/user/.local/bin:$PATH"

WORKDIR /app

COPY --chown=user ./requirements.txt requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY --chown=user . /app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "7860"]
```

### `requirements.txt`

```txt
fastapi
uvicorn
requests
pydantic<2
```

---

## ✅ Cómo probarlo localmente

1. Clonar este repositorio: 
```
git clone https://github.com/LuisCerelli/ChatBot_AHdC.git
cd ChatBot_AHdC
```

2. Cambiar el nombre del archivo ```.envprueba``` por el de ```.env``` y colocar en él la Key de [HuggingFace](https://huggingface.co/LuisDSAI)
3. Recomendamos, para evitar problemas de compatibilidad entre dependencias, utilizar este proyecto en un entorno virtual, para ello debemos crear y activar estos comandos:
**En MacOs/Linux:**
```
python3 -m venv venv
source venv/bin/activate
```
**En Windows**:
```
python -m venv venv
venv\Scripts\activate
```
* Una vez activado el entorno, instalar las dependencias del proyecto con:
```
pip install -r requirements.txt
```
<u>**Importante**</u>: Esto asegura que todas las librerías necesarias se instalen en versiones compatibles, tal como fueron definidas en el archivo requirements.txt, evitando conflictos con otras instalaciones globales de Python.


4. Asegurarse de tener un entorno local (por ejemplo, abrir `huella_local.html` con <u>Live Server</u> o <u>Visual Studio Code</u>).
5. El HTML llama al backend a través del script `chatbot.js`.
6. El backend debe estar **activo en Hugging Face Spaces**.
7. Si todo está bien configurado, el chat responderá normalmente al enviar mensajes.

---

## 🧪 Cómo hacer debug si deja de funcionar

- Verificar que el Space **no esté pausado** o en error:
  - [https://huggingface.co/spaces](https://huggingface.co/spaces)

- Revisar los **logs del Space** en la pestaña *"Logs"*.
- Verificar el `HF_TOKEN` cargado como secreto en Hugging Face.
- Verificar que el endpoint en `chatbot.js` coincida con el Space activo.
- Confirmar que `chatbot.js` está bien enlazado en el HTML y sin errores JS.
- Si algo falla, **crear un nuevo Space limpio** con los mismos archivos (suele resolver bloqueos inexplicables).

---

## 👤 Contacto del colaborador

Este sistema fue actualizado e implementado por:

**Luis Cerelli**  
Colaborador voluntario  
📩 *Para consultas técnicas o inconvenientes relacionados con la clave de [HuggingFace](https://huggingface.co/) o el acceso a la plataforma, no dudes en contactarme.*

📧 [Mail: luisalberto.cerelli@asociacionhuelladecarbono.org](luisalberto.cerelli@asociacionhuelladecarbono.org)  
🔗 [GitHub: @LuisCerelli](https://github.com/LuisCerelli)

---

## 🟢 Estado del proyecto

🟢 100% operativo  
📦 Backend funcionando en Hugging Face  
🌱 Listo para integración en la web oficial de la Asociación

---

## 🧠 Futuras mejoras sugeridas

- Mejora de las posibles alucinaciones mediante la provision de documentos de la Asociación (RAG)
- Mejora del Front a evaluar con el equipo de diseño 
- Soporte para historial de conversación
- Traducción automática desde otros idiomas
- Modo oscuro integrado al sistema
- Interacción por voz (Web Speech API)
- Analítica de uso del chatbot

---

## 🙌 Gracias

Gracias a la Asociación Huella de Carbono por confiar en la tecnología y la IA para promover la sostenibilidad. Este chatbot es solo el primer paso hacia una comunicación automatizada y accesible.



