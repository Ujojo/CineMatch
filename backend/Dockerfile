# 1. Image de base légère Python 3.12
FROM python:3.12-slim

# 2. Empêche Python d'écrire des fichiers .pyc sur le disque et force l'affichage immédiat des logs
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 3. Répertoire de travail dans le conteneur
WORKDIR /app

# 4. Installation des dépendances système nécessaires (notamment pour psycopg2 / PostgreSQL)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# 5. Copie et installation des dépendances Python
COPY requirements.txt /app/
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# 6. Copie du reste du code source de l'application
COPY . /app/

# 7. Exposition du port 8000
EXPOSE 8000

# 8. Commande de lancement du serveur FastAPI avec Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]