from django.urls import path
from .views import view_machine, machines, logout_user


urlpatterns = [
    path('machine/<str:MachineID>' , view_machine, name ='view-machine'),
    path('machines/',machines , name = 'list-machines' ),
    path('logout/' , logout_user, name = 'logout')
]