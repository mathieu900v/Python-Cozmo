# Configuration du RPI

En arrivant ici, vous êtes théoriquement  avec un RPI branché sur un écran et un clavier.

Sur votre terminal taper les commandes suivants:
```
user:~$ sudo apt-get update
```
```
user:~$ sudo apt-get upgrade
```
<b>!!!Attention cette action peut prendre énormément de temps !!!</b>
```
user:~$ sudo apt install python3.9
```
```
user:~$ sudo apt-get install git
```
Le RPI (Raspberry PI) doit pouvoir se connecter par USB à la tablette pour cela il faut installer un nouveau paquet <i>usbmuxd</i>
```
user:~$ sudo apt-get install usbmuxd
```

Pour utiliser python il est quasiment impératif d'utiliser des virtualenvs, pour cela je vais vous faire suivre un tutoriel simplifiant leur utilisation. Suivez le tuto suivant avec pour nom de virtualenv <b>cozmo</b>
[Lien du tuto](./VirtualenvWrapper.md)

Vous êtes censé avoir un virtualenv actif du nom de cozmo, nous allons donc maintenant récupérer le projet et installer les requierements:
Si vous n'avez pas de virtualenv actif pensé à l'activer:
```
user:~$ workon cozmo
(cozmo) user:~$
```
```
(cozmo) user:~$ git pull git@git.unistra.fr:mazzarella/lo6-projet-python.git
```
ou en https:
```
(cozmo) user:~$ git pull https://git.unistra.fr/mazzarella/lo6-projet-python.git
```

Dans la racine du projet il existe un dossier <i>requierement.in</i>
```
(cozmo) user:~$ cd lo6-project-python
(cozmo) user:~/lo6-project-python$ pip install -r requierement.in
```

Vous pouvez dès à présent connecter l'Ipad au RPI et lancer le serveur
```
(cozmo) user:~/lo6-project-python$ cd website

#Première fois
(cozmo) user:~/lo6-project-python/website$ python manage.py migrate

(cozmo) user:~/lo6-project-python/website$ python manage.py runserver
```
Il vous faudra maintenant récupérer l'ip du RPI et le site est accessible

```
(cozmo) user:~/lo6-project-python/website$ ip addr
```

Pour aller plus loin et avoir un auto login + mise en route automatique du serveur veuillez suivre le tuto suivant
[Plus de configuration](./04_Plus_Configuration.md)

<i>Rapport rédigé par Samuel Ladwein, Enzo Mozzarella, Serkan Deveci, Mathieu Voyer</i>
