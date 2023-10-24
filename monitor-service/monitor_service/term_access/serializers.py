from rest_framework import serializers
from .models import Installed_App, Running_Apps


class Installed_app_serializer(serializers.ModelSerializer):
    class Meta:
        model = Installed_App
        fields= "__all__"
    
    


class RunningAppsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Running_Apps
        fields = "__all__"

