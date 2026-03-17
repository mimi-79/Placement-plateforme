F# Utiliser une image Python légère
FROM python:3.11-slim

# Définir le dossier de travail dans le conteneur
WORKDIR /app

# Copier le fichier des dépendances
COPY requirements.txt .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install gunicorn

# Copier tout le reste du code
COPY . .

# Exposer le port que Flask/Gunicorn va utiliser
EXPOSE 5000

# Commande pour lancer l'application avec Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "routes:app"]