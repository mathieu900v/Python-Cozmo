from django.db import models
 
# Create your models here.  
class Member(models.Model):
    username=models.CharField(max_length=50)
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    password=models.CharField(max_length=20)
 
    def __str__(self):
        return self.firstname + " " + self.lastname
   
  
    class Meta:  
        db_table = "website_cozmo"



class Game(models.Model):
    title=models.CharField(max_length=50)
    description=models.CharField(max_length=200)
    file=models.CharField(max_length=200)
   
    class Meta:  
        db_table = "game"

