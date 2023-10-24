
import os

import requests
import json



Allowed_Values = {             
"Host Name" ,             
"OS Name" ,                 
"OS Version",             
"OS Manufacturer" ,         
"OS Configuration",        
"Registered Owner",        
"System Manufacturer",     
"System Model" ,          
"System Boot Time" ,            
"Original Install Date" ,  
"BIOS Version" ,  
"Boot Device",             
"System Locale",           
"Input Locale",             
"Time Zone",               
"Total Physical Memory", 
"Available Physical Memory",
      }


def send_get_request(machineID):
    try:
        
        url = "http://127.0.0.1:8000/machine/status/" + str(machineID)

        response = requests.get(url)
        
        return response
    except requests.exceptions.RequestException as e:
        # Handle any exceptions that may occur during the request
        print(f"Error sending GET request: {e}")
        return None
def send_post_request(data_dict , headers = None):
    try:
        # Convert the dictionary to a JSON string
        json_data = json.dumps(data_dict)
        

        # Set the headers for the request (including content type)
        if headers is None:
            headers = {'Content-Type': 'application/json'}

        # Send the POST request with the JSON data
        response = requests.post("http://127.0.0.1:8000/machine/create/", data=json_data, headers=headers)
        
        # Check if the request was successful
        response.raise_for_status()
        return response
    except requests.exceptions.RequestException as e:
        # Handle any exceptions that may occur during the request
        print(f"Error sending POST request: {e}")
        return None
def send_put_request(machineID , data_dict , headers = None):
    try:
        # Convert the dictionary to a JSON string
        json_data = json.dumps(data_dict)
        
        
        # Set the headers for the request (including content type)
        if headers is None:
            headers = {'Content-Type': 'application/json'}

        # Send the POST request with the JSON data
        url = "http://127.0.0.1:8000/machine/status/" + str(machineID)
        response = requests.put(url, data=json_data, headers=headers)
        
        # Check if the request was successful
        response.raise_for_status()
        return response
    except requests.exceptions.RequestException as e:
        # Handle any exceptions that may occur during the request
        print(f"Error sending PUT request: {e}")
        return None            


def generate_spec_dictionary(string):
    machine_spec = {}
    lines = string.split('\n')

    for line in lines:
        key = line.split(':')[0]
        
        if key in Allowed_Values:
            key = key.replace(' ', '_')
            value = line.split(':')[1]
            value = ' '.join(value.split())
            machine_spec[key] = value
    
    return machine_spec
def get_systeminfo(my_socket , machineID):
    print("Gathering System Info")
    command = "systeminfo"
    my_socket.send_data(command)
    #add sleep
    
    get_response = send_get_request(machineID=machineID)
    
    result = my_socket.recieve_data()
    

    specs = generate_spec_dictionary(result)
    if(get_response.status_code == 404):
        
        specs['machine_ID'] = machineID
        send_post_request(specs)
    else:
        specs['machine_ID'] = machineID
        send_put_request(machineID , specs )


def generate_Installed_apps_list(string):
    installed_apps = []
    lines = string.split('\n')
    

    for line in lines[3:20]:
        
        app_name = line.split('.')[1]
        app_name = ' '.join(app_name.split())
        installed_apps.append(app_name)
    
    return installed_apps
    

def send_delete_request_IA(machineID):
    try:

        url = "http://127.0.0.1:8000/monitor/installed_apps/" + str(machineID)
        
        response = requests.delete(url )
        
        return response
    except requests.exceptions.RequestException as e:
        # Handle any exceptions that may occur during the request
        print(f"Error sending DELETE request: {e}")
        return None
def send_post_request_IA(machineID, list_of_apps, headers = None):
    try:
        # Convert the dictionary to a JSON string
        string_of_apps = ','.join(list_of_apps)
        test ={
        
        "machine_ID": str(machineID),
        "installed_apps": string_of_apps
        }
        json_data = json.dumps(test)
        

        # Set the headers for the request (including content type)
        if headers is None:
            headers = {'Content-Type': 'application/json'}

        # Send the POST request with the JSON data
        url = "http://127.0.0.1:8000/monitor/installed_apps/"
        response = requests.post(url, data=json_data, headers=headers)
        
        # Check if the request was successful
        response.raise_for_status()
        return response
    except requests.exceptions.RequestException as e:
        # Handle any exceptions that may occur during the request
        print(f"Error sending POST request: {e}")
        return None

def running_app_list(string):
    running_apps = []
    lines = string.split('\n')
    

    for line in lines[3:11]:
        
        app_name = line
        app_name = ' '.join(app_name.split())
        running_apps.append(app_name)
    
    return running_apps

def send_post_request_RA(machineID, list_of_apps, headers = None):
    try:
        # Convert the dictionary to a JSON string
        string_of_apps = ', '.join(list_of_apps)
        test ={
        
        "machine_ID": str(machineID),
        "running_apps": string_of_apps
        }
        json_data = json.dumps(test)
        
        
        # Set the headers for the request (including content type)
        if headers is None:
            headers = {'Content-Type': 'application/json'}

        # Send the POST request with the JSON data
        url = "http://127.0.0.1:8000/monitor/running_apps/"
        response = requests.post(url, data=json_data, headers=headers)
        
        # Check if the request was successful
        response.raise_for_status()
        return response
    except requests.exceptions.RequestException as e:
        # Handle any exceptions that may occur during the request
        print(f"Error sending POST request: {e}")
        return None
def send_delete_request_RA(machineID):
    try:
        
        url = "http://127.0.0.1:8000/monitor/running_apps/" + str(machineID)
        
        response = requests.delete(url)
        
        return response
    except requests.exceptions.RequestException as e:
        # Handle any exceptions that may occur during the request
        print(f"Error sending DELETE request: {e}")
        return None
    





def handleConnection(my_socket , machineID):
    print("[+] Handling Connection with :", {machineID})


    ## handle systeminfo
    get_systeminfo(my_socket , machineID)






    ## handle installed apps

    print("Installed Apps  ")
    command = "Get-AppxPackage -AllUsers | Select Name"
    my_socket.send_data(command)
    
    result = my_socket.recieve_data()
    IA_List = generate_Installed_apps_list(result)
    
    send_delete_request_IA(machineID)
    send_post_request_IA(machineID=machineID, list_of_apps=IA_List)
    
    



    ## handle running apps
    print("Saving Running apps")
    command = "Get-Process | Sort-Object -Property 'CPU' -Descending | Select-Object -First 10 | Select ProcessName"
    my_socket.send_data(command)
    
    result = my_socket.recieve_data()
    RA_List = running_app_list(result)
    
    
    send_delete_request_RA(machineID)

    send_post_request_RA(machineID=machineID, list_of_apps=RA_List)
    



