from django.shortcuts import render, redirect
from client.models import Machine
from term_access.models import Installed_App, Running_Apps

from django.contrib.auth import authenticate , login, logout

from django.contrib import messages

# Create your views here.

def machines(request):
    context = {}
    
    machines = Machine.objects.all()
    context['machines'] = machines

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request , username = username , password = password )

        if user is not None:
            login(request , user)
            messages.success(request , "Logged in!")
            return redirect('list-machines')
        else:
            messages.success(request , "Login Failed!")
            return redirect('list-machines')   

    return render(request , "machines.html" , context )

def logout_user(request):
    logout(request)
    messages.success(request, "Logged out!")
    return redirect('list-machines')



def view_machine(request , MachineID):
    if request.user.is_authenticated:
        machine_specs = Machine.objects.get(machine_ID = MachineID)
        

        context = {}
        context['machine'] = machine_specs


        installed_apps = Installed_App.objects.get(machine_ID = MachineID)
        
        context['installed_apps'] = str(installed_apps).split(',')[1:]

        running_apps = Running_Apps.objects.get(machine_ID  =MachineID)
        context['running_apps']= str(running_apps).split(',')[1:]

    else:
        print("login first")

    return render(request , "view_machine.html", context)

