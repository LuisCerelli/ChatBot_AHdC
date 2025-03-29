# Dockerfile recomendado por Hugging Face adaptado para FastAPI

FROM python:3.11

# Crear usuario no-root y cambiar a él
RUN useradd -m -u 1000 user
USER user
ENV PATH="/home/user/.local/bin:$PATH"

WORKDIR /app

# Copiar requirements.txt y usar el usuario correcto
COPY --chown=user ./requirements.txt requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Copiar el resto del código
COPY --chown=user . /app

# Comando para lanzar FastAPI en puerto 7860
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "7860"]

