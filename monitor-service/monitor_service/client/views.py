from django.shortcuts import render
from django.core.exceptions import ValidationError
from rest_framework.views import APIView
from rest_framework import generics, mixins
from rest_framework import status
from rest_framework.response import Response
from .models import Machine
from .serializers import MachineSerializer
# Create your views here.



class CreateMachine(APIView):
    def post(self, request):
        serializer = MachineSerializer(data = request.data)

        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data , status = status.HTTP_200_OK)
        
        return Response(serializer.errors , status = status.HTTP_400_BAD_REQUEST)
    

class MachineAV(APIView):
    def get_object(self , primaryKey):
        try:
            print("finding nemo", primaryKey)
            return Machine.objects.get(machine_ID = primaryKey)
        except Machine.DoesNotExist:
            return None
        
    def get(self , request , MachineID):
        
        machine = self.get_object(MachineID)
        if machine is not None:
            serializer = MachineSerializer(machine)
            return Response(serializer.data)
        else:
            print("no machine with this machine_ID")

            return Response({'ERROR': 'Object Does not exist'}, status=status.HTTP_404_NOT_FOUND)
    def put(self, request, MachineID):
        
        print(MachineID)
        machine = self.get_object(MachineID)

        serializer = MachineSerializer(machine , data = request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors , status = status.HTTP_400_BAD_REQUEST)
    
    def delete(self , request , MachineID):
        machine = self.get_object(primaryKey= MachineID)
        machine.delete()

        return Response(status = status.HTTP_204_NO_CONTENT)
    





    
    

        