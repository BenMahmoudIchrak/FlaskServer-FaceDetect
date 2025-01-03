## Facial Recognition API Flask

![Facial Recognition API](https://via.placeholder.com/800x300.png?text=Facial+Recognition+API)



## Description

**FlaskServer-FaceDetect** est un projet de reconnaissance faciale transformé en API serveur à l'aide de **Flask**. Il permet d'effectuer une détection et une reconnaissance faciale à partir d'images envoyées via des requêtes HTTP. Ce service expose une API que vous pouvez consommer dans n'importe quelle application cliente pour ajouter des fonctionnalités de reconnaissance faciale.

L'API utilise **OpenCV** et **Python** pour effectuer la détection et la comparaison faciale, renvoyant un pourcentage de compatibilité pour chaque reconnaissance.

## Fonctionnalités

- **Détection Faciale** : Localisation des visages dans une image.
- **Reconnaissance Faciale** : Identification des visages avec un score de compatibilité.
- **API RESTful** : L'API expose des endpoints pour traiter les images et renvoyer des résultats de reconnaissance.

## Installation

### Prérequis

Assurez-vous d'avoir installé Python 3.x sur votre machine. Si ce n'est pas déjà fait, vous pouvez le télécharger ici : [Python.org](https://www.python.org/).

### Installation des dépendances

Clonez ce dépôt, puis installez les dépendances à l'aide de `pip` :

```bash
git clone https://github.com/BenMahmoudIchrak/FlaskServer-FaceDetect.git
cd FlaskServer-FaceDetect

