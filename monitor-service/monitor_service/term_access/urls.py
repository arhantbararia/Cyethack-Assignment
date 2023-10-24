from django.urls import path
from .views import InstallApp,InstallApp_Detail, RunnApp_Detail , RunnApp


urlpatterns = [
    path('installed_apps/<str:MachineID>' , InstallApp_Detail.as_view(), name = 'installed_app-detail'),
    path('installed_apps/', InstallApp.as_view(), name = 'installed_apps' ),

    path('running_apps/<str:MachineID>' , RunnApp_Detail.as_view(), name = 'running_apps-detail'),
    path('running_apps/', RunnApp.as_view(), name = 'running_apps' )

    
    
]