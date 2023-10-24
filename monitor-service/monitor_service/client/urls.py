from django.urls import path
from .views import CreateMachine, MachineAV


urlpatterns = [
    path('create/' , CreateMachine.as_view(), name ='create-machine'),
    path('status/<str:MachineID>', MachineAV.as_view(), name = 'machine-details')    


]