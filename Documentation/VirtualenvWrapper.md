# Virtualenvwrapper est une extension simplifiant l'utilisation des virtualenv python



[Lien d'installation](https://virtualenvwrapper.readthedocs.io/en/latest/)

```console
user:~$ pip3 install virtualenvwrapper
# Installation terminé
# Il va falloir initialisé quelque variable
user:~$ vim ~/.bashrc
```
Ajouter les lignes suivantes en fin de fichier
```
export WORKON_HOME=$HOME/.virtualenvs  
export VIRTUALENVWRAPPER_PYTHON=$(which python3)  
export PROJECT_HOME=$HOME/{PATH_PROJECT}  
source /usr/local/bin/virtualenvwrapper.sh
```
```{PATH_PROJECT}``` => Correspond au dossier contenant tous vos projets

Vous pourrez ensuite redémarrer la machine.

## Utilisation
Création d'un virtualenv:
```
user:~$ mkvirtualenv {NOM_VIRTUAL_ENV}
(NOM_VIRTUAL_ENV) user:$
```

Utiliser un virtualenv existant:
```
user:~$ workon {NOM_VIRTUAL_ENV}
# L'autocomplétion propose les noms de vos virtualsenvs
(NOM_VIRTUAL_ENV) user:$
```
Quitter un virtualenv:
```
(NOM_VIRTUAL_ENV) user:~$ deactivate
user:$
```
Liste les packages du virtualenv actif:
```
(NOM_VIRTUAL_ENV) user:~$ lssitepackages

```

Supprimer un virtualenv:
```
(NOM_VIRTUAL_ENV) user:~$ deactivate
user:~$ rmvirtualenv (NOM_VIRTUAL_ENV)
```
