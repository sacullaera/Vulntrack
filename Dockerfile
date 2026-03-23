FROM python:3.11-slim

# Define o diretório de trabalho
WORKDIR /app

# Instala dependências de sistema (se necessário)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /app/data && chmod 777 /app/data

# Instala dependências do Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o código do projeto
COPY . .

# Coleta arquivos estáticos (opcional, depende de como você serve static)
RUN python manage.py collectstatic --noinput

# Expõe a porta do Django
EXPOSE 8000

# Comando padrão (será sobrescrito no docker-compose para o worker)
CMD ["gunicorn", "vultrack.wsgi:application", "--bind", "0.0.0.0:8000"]