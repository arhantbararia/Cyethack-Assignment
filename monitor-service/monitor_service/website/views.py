from django.shortcuts import render
from client.models import Machine
from term_access.models import Installed_App, Running_Apps
from django.contrib import messages

# Create your views here.

def machines(request):
    context = {}
    if request.user.is_authenticated:
        machines = Machine.objects.all()
        context['machines'] = machines

    return render(request , "machines.html" , context )



def view_machine(request , MachineID):
    if request.user.is_authenticated:
        machine_specs = Machine.objects.get(machine_ID = MachineID)
        

        context = {}
        context['machine'] = machine_specs


        installed_apps = Installed_App.objects.get(machine_ID = MachineID)
        
        context['installed_apps'] = str(installed_apps).split(',')

        running_apps = Running_Apps.objects.get(machine_ID  =MachineID)
        context['running_apps']= str(running_apps).split(',')

    else:
        print("login first")

    return render(request , "view_machine.html", context)

