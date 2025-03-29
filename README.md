# 📄 — *Chatbot Huella de Carbono* 🌱🤖


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
https://<nombre-del-space>.hf.space/chat
```

*(Reemplazar `<nombre-del-space>` con el nombre real del Space activo)*

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

1. Asegurarse de tener un entorno local (por ejemplo, abrir `huella_local.html` con Live Server o Visual Studio Code).
2. El HTML llama al backend a través del script `chatbot.js`.
3. El backend debe estar **activo en Hugging Face Spaces**.
4. Si todo está bien configurado, el chat responderá normalmente al enviar mensajes.

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

## ✍️ Personalización

- Cambiar el avatar: reemplazar la imagen en `/Imagenes-logos/icono/`.
- Editar mensajes predefinidos: en `chatbot.js` (`setQuickQuestion(...)`).
- Ajustar colores o animaciones: en `styles.css`.
- Se puede conectar a otro modelo o API modificando `main.py`.

---

## 👤 Contacto del colaborador

Este sistema fue actualizado e implementado por:

**Luis Cerelli**  
Colaborador voluntario  
📧 [opcional]  
🔗 [GitHub: @LuisCerelli](https://github.com/LuisCerelli)

---

## 🟢 Estado del proyecto

🟢 100% operativo  
📦 Backend funcionando en Hugging Face  
🌱 Listo para integración en la web oficial de la Asociación

---

## 🧠 Futuras mejoras sugeridas

- Soporte para historial de conversación
- Traducción automática desde otros idiomas
- Modo oscuro integrado al sistema
- Interacción por voz (Web Speech API)
- Analítica de uso del chatbot

---

## 🙌 Gracias

Gracias a la Asociación Huella de Carbono por confiar en la tecnología y la IA para promover la sostenibilidad. Este chatbot es solo el primer paso hacia una comunicación automatizada y accesible.



