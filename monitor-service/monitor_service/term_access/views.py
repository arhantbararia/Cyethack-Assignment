from django.shortcuts import render
from django.core.exceptions import ValidationError
from rest_framework.views import APIView
from rest_framework import generics, mixins
from rest_framework import status
from rest_framework.response import Response
from .models import Installed_App, Running_Apps
from .serializers import Installed_app_serializer, RunningAppsSerializer

# Create your views here.

class InstallApp(APIView):

    def get(self, request):
        installed_apps = Installed_App.objects.all()

        serializer = Installed_app_serializer(installed_apps, many = True)
        return Response(serializer.data)
    


    def post(self, request):
        serializer = Installed_app_serializer(data = request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data , status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors , status= status.HTTP_400_BAD_REQUEST)

    
        

        
class InstallApp_Detail(APIView):
    def get_object(self , primaryKey):
        try:
            print("finding nemo", primaryKey)
            return Installed_App.objects.get(machine_ID = primaryKey)
        except Installed_App.DoesNotExist:
            return None 

    def get(self, request, MachineID):
        installed_apps = self.get_object(primaryKey = MachineID)

        if not installed_apps:
            # If there are no instal led apps, return a 404 response
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = Installed_app_serializer(installed_apps, many=True)
        return Response(serializer.data)
    
    def delete(self, request, MachineID):
        try:
            print('Inside the delete function for installed apps')

            app_data = self.get_object(primaryKey=MachineID)

            if app_data is not None:
                app_data.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            else:
                # Handle the case where the object does not exist
                return Response({'error': 'Object does not exist'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': f'Error: {e}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    




class RunnApp(APIView):
    def get(self, request):
        running_apps = Running_Apps.objects.all()

        serializer = RunningAppsSerializer(running_apps, many = True)
        return Response(serializer.data)
    


    def post(self, request):
        serializer = RunningAppsSerializer(data = request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data , status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors , status= status.HTTP_400_BAD_REQUEST)

    
        

        
class RunnApp_Detail(APIView):


    def get_object(self , primaryKey):
        try:
            print("finding nemo", primaryKey)
            return Running_Apps.objects.get(machine_ID = primaryKey)
        except Running_Apps.DoesNotExist:
            return None 

    def get(self, request, MachineID):
        running_apps  = self.get_object(primaryKey = MachineID)

        if not running_apps:
            # If there are no instal led apps, return a 404 response
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = RunningAppsSerializer(running_apps, many=True)
        return Response(serializer.data)
    
    def delete(self, request, MachineID):
        try:
            print('Inside the delete function for running')

            app_data = self.get_object(primaryKey=MachineID)

            if app_data is not None:
                app_data.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            else:
                # Handle the case where the object does not exist
                return Response({'error': 'Object does not exist'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': f'Error: {e}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

