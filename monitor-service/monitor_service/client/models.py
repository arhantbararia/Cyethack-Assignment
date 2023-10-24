from django.db import models

# Create your models here.
class Machine(models.Model):
    machine_ID =                 models.CharField(max_length= 100 , primary_key= True )
    Host_Name =                 models.CharField(max_length = 200, null = True)
    OS_Name =                   models.CharField(max_length = 200, null = True)
    OS_Version =                models.CharField(max_length = 200, null = True)
    OS_Manufacturer =           models.CharField(max_length = 200, null = True)
    OS_Configuration =          models.CharField(max_length = 200, null = True)
    Registered_Owner =          models.CharField(max_length = 200, null = True)
    System_Manufacturer=       models.CharField(max_length = 200, null = True)
    System_Model =             models.CharField(max_length = 200, null = True)
    System_Boot_Time =         models.CharField(max_length = 200, null = True)
    Original_Install_Date =    models.CharField(max_length = 200, null = True)
    BIOS_Version =             models.CharField(max_length = 200, null = True)
    Boot_Device=                models.CharField(max_length = 200, null = True)
    System_Locale=              models.CharField(max_length = 200, null = True)
    Input_Locale=              models.CharField(max_length = 200, null = True)
    Time_Zone=                models.CharField(max_length = 200, null = True)
    Total_Physical_Memory =    models.CharField(max_length = 200, null = True)
    Available_Physical_Memory = models.CharField(max_length=200 , null = True )
    

    def __str__(self):
        return self.Host_Name

    