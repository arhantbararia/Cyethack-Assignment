from django.urls import path
from .views import view_machine, machines


urlpatterns = [
    path('machine/<str:MachineID>' , view_machine, name ='view-machine'),
    path('machines/',machines , name = 'list-machines' )
]