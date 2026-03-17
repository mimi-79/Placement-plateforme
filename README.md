## Plateforme de Placement Étudiant

Ce projet est une application web développée avec **Flask** permettant de centraliser et de gérer les demandes de stage des étudiants. L'application est entièrement conteneurisée avec **Docker** pour garantir un lancement rapide et sans erreur sur n'importe quelle machine.

##  Description du projet
L'application propose une interface simple pour :
* Saisir les informations d'une demande de stage (ID et Titre du projet).
* Sauvegarder les données via un serveur Flask.
* Automatiser la construction de l'image grâce à un pipeline **CI/CD** (GitHub Actions).

## Pour lancer le projet sur votre machine :
1. `docker build -t docker build -t app-demandes-img .
2. `docker run -p 5000:5000 app-demandes-img`
Accédez ensuite à `http://localhost:5000`
