from django.db import models
from client.models import Machine
import json

# Create your models here.


class Installed_App(models.Model):
   
    
   machine_ID = models.CharField(max_length=200 , primary_key= True)
   installed_apps = models.TextField()  ## data needs to be serialized before dumping
   
   
   
   def __str__(self):
      
      return f"'installed_apps':{self.installed_apps}"
                                        

    
    
    
  


class Running_Apps(models.Model):
    machine_ID = models.CharField(max_length=200 , primary_key= True)
    running_apps = models.TextField()  ## data needs to be serialized before dumping
                                        ## and needs to de-serialized after loading

    def __str__(self):
      
      return f"''running_apps':{self.running_apps}"


    

