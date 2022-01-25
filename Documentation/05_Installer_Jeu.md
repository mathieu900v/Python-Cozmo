# Installer votre propre jeu

Rien de plus simple pour installer votre jeu,
Dans la base de données du site rajouté une nouvelle ligne (qu'elle que soit la manière) dans la table <b>game</b>

La table Game est constituée de 4 champs : Voici sa composition avec un exemple 

| id  | title  | description | file |
|---|---|---|---|
| 5  | Uno | Jeu du Uno avec cozmo  | uno  |

où file est le nom du fichier sans l'extension .py

Ensuite il vous faudra ajouter sur le RPI dans le dossier game/ votre fichier renommé correctement, dans notre exemple uno


Si vous devez utiliser une base de données dans votre jeu, déplacez votre .db dans le dossier game_bdd (préférez le même nom que le .py)
Et dans votre fichier .py accéder à la base de données de la même manière que dans notre fichier exemple quizz.py

Si votre jeu possède des imports particulier, type sqlite3, pensez bien à rajouter ces mêmes imports dans view.py, dans le cas contraire, si vous oubliez l'import, une erreur `name "machin" is not defined `apparaitra. 

<i>Rapport rédigé par Samuel Ladwein, Enzo Mozzarella, Serkan Deveci, Mathieu Voyer</i>
