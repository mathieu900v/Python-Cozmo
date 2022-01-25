# Installation du RPI

Ce tuto vous permettra d'installer Ubuntu-server 20.04.3 LTS:

   - Ubuntu-server car la distribution Debian n'est pas compatible avec l'API Cozmo
   - LTS pour Long term Service, qui signifie que l'OS sera mis à jour pendant longtemps
   - La version server est la seule bonne version d'Ubuntu qui ne demande pas de ressources graphiques au Raspberry Pi, ce qui entrainerait des latences et des complications.
    
J'ai choisi d'utiliser l'application <b>Balena Etcher</b> pour flasher ma carte SD puisque c'est un logiciel très simple d'utilisation, il faudra donc au préalable installer cette application.
    
   1. J'insère la carte Micro SD dans mon PC portable (si aucun port n'est présent sur votre pc pour le faire il vous faudra trouver un adaptateur)
   2. Je lance Balena Etcher
   3. Je télécharge la version **Ubuntu-server 20.04.3 LTS** au format **ARM64** puisque c'est l'architecture processeur du Raspberry Pi: [Lien d'installation](https://ubuntu.com/download/server/arm)
   4. Je flash la carte SD avec le fichier .iso téléchargé (cela peut prendre du temps)
   5. Si tout s'est bien passé (le logiciel le dirait dans le cas contraire), je retire la carte SD en l'éjectant
   6. Je mets la carte SD dans le slot du Raspberry Pi
    
    ## Premier démarrage
    
   1. Je branche en premier les périphériques (écran, clavier) et le câble réseau
   2. Puis en dernier l'alimentation, puisqu'il va démarrer instantanément
   3. Le démarrage peut être long, il va d'abord décompresser des fichiers (~3min)
   4. Il y a des écrans de configuration dans lesquels il faudra naviguer avec les flèches et la touche Entrée du clavier
   5. D'abord la configuration de la langue (ici FR)
   6. Du type de clavier (ici 105Keys)
   7. Choix du mot de passe pour l'utilisateur de base ubuntu, puis connexion dans les tty (consoles linux)
   8. Et voilà le Raspberry Pi est maintenant fonctionnel

<i>Rapport rédigé par Samuel Ladwein, Enzo Mozzarella, Serkan Deveci, Mathieu Voyer</i>
