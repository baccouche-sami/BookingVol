

# A Propos:

Booking App est une application developpée pour mettre en oeuvre les bonnes pratiques en Architecture Logiciel.

Le but c'est d'apprendre à developper les solution informatique tout en tenant compte les evolutions future de de cette application

##  Membres :

1- Mame yacine Camara

2- Nanon Abdul-Aziz  Ouattara

3- Sami Baccouche

4- Aguibou Barry

# Front-end:

Le coté  frontend à été developpé en vue.js, pour la mise en forme des pages nous avons utliser la bibliothèque tailwind css et HeadLess ui

## Choix de cette technologie: cette technologie à été choisie car la majorité l'avait déja utilisé et donc cela faciliterai le travail de groupe.

 ##Communication avec le back-end: pour envoyer des requetes depuis la partie front-end de l'application, nous avons utilisé axios.
 L'application est 100% responsive pour s'adapter à tout type d'ecran.
 
 #Lancement Front-end: pour demarrer l'application coté front-end on fait:
 
 On accede au repertoire du front-end qui setrouve dans 'BookingVol/frontend', ensuite on fait:
  ``npm intall`` (pour installer toutes les dependances neccessaires), ensuite 
  ``npm run dev`` (pour demarrer l'application)

# Back-end:

Le coté Back-end à été codé à l'aide du framework python Django + Django Rest Framework.



# Structure du backend:

Dans le répertoire les modèles de notre BD sont accessibles sous backend/booking/booking_app/models/

Le dossier backend/booking/booking_app/api contient les différentes classes et methodes utilisées pour la structuration de notre REST API:

- dans serializers.py on defini la forme attendue ou retournée pour les différentes requetes avec chacun de nos modèles.

- dans filters.py on défini les champs de nos modèles sur les lequels il est possible de filtrer depuis la requetes et comment réagir à ces demandes de filtre.

- dans viewsets.py on défini on prépare les informations renvoyé lors des appels à nos services et on surchages nos verbes http si besoin

- dans views.py on fait plus ou moins pareil que dans viewsets.py mais pour les informations externes à notre systeme.

- dans utils.py on definit différentes méthodes utilitaires utiles à notre API et réutilisées à différents endroits.

- dans route.py on fait le routage pour nos modeles internes en assignant à chacune de nos route un viewsets (on utilisera ensuite ce router dans nos endpoints finaux).


le fichier backend/booking/booking/urls.py gère la définition des différents endpoints de notre API. booking/ pour les internes et booking/external pour les services externes.


# setup

## installation ou mise à jour python

- Si vous n'avez pas du tout python suivez l'un de ces tutoriels en fonction de votre système d'exploitation :

  1. [Linux](https://www.makeuseof.com/install-python-ubuntu/)
  2. [Mac](https://docs.python-guide.org/starting/install3/osx/)
  3. [Windows](https://www.pythontutorial.net/getting-started/install-python/)
  4. or dowload installer [here](https://www.python.org/)

## installation pipenv

1.depuis votre terminal executez la commande <span style="color:black;background-color:lightgrey">*pip install pipenv*</span>.

2.depuis backend/booking executez <span style="color:black;background-color:lightgrey">*pipenv install*</span> puis <span style="color:black;background-color:lightgrey">*pipenv shell*</span>.

3.Vous disposez maintenant d'un environnement pour lancer notre serveur

# lancement de l'api

depuis backend/booking executer :

- <span style="color:black;background-color:lightgrey">*python manage.py makemigrations*</span>
- <span style="color:black;background-color:lightgrey">*python manage.py migrate*</span>
- <span style="color:black;background-color:lightgrey">*python manage.py runserver*</span>

une fois ces commandes executées, depuis le navigateur saisir :
- <span style="color:black;background-color:lightgrey">http://localhost:8000/booking</span> pour les routes des modeles par internes. (Depuis cette interface vous aurez accès aux données stockés et pourrez réaliser toutes les actions CRUD.) 
- ou <span style="color:black;background-color:lightgrey">http://localhost:8000/booking/external</span> pour visualiser les vols externes.

