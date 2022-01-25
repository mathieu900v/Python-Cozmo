# Plus de configuration avec le RPI

## Lancer au boot le server python
```
user:~$ sudo -i
root:~$ mkvirtualenv cozmo
(cozmo) root:~$ pip install -r ../home/<CheminAbsolue>/requirement.in

root:~$ vim ~/.bashrc
```    
Ajoutez à la fin du fichier:
    
   ```
   workon cozmo
   python ../home/$CHEMIN/manage.py runserver
   ```
$CHEMIN = Il s'agit du chemin ABSOLUE vers le manage.py de votre application fraichement installé

<i>Rapport rédigé par Samuel Ladwein, Enzo Mozzarella, Serkan Deveci, Mathieu Voyer</i>
