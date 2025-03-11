# Use uma imagem oficial do Python como base
FROM python:3.10-slim

# Instala dependências do sistema para compilar pacotes Python como psycopg2
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia os arquivos de dependências para o container
COPY requirements.txt .

# Instala as dependências do Python
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do código da aplicação
COPY . .

# Expõe a porta do FastAPI (se aplicável)
EXPOSE 8000

# Comando de entrada para rodar a aplicação
CMD ["python", "main.py"]
