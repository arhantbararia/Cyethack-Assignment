# Monitor Service

Monitor service aims to provide a monitoring service to get the status of members of a cluster of computers. It uses socket communication to talk to Remote Server (Master). This also provides an interface to the administrator to view and manage the slave machines. Uses MySQL to store data.

This is a guide to show the process of installation and setting up and examples.

### Installation

To set up monitor service, follow these steps:

1. Make sure you have python installed on Master machine.
2. Clone this git repository to your master machine.
    
    ```python
    git clone https://github.com/arhantbararia/Cyethack-Assignment.git
    ```
    
3. Navigate to Django web server folder using:
    
    ```python
    cd Cytehack-Assignment/monitor-service/monitor_service
    ```
    
4. Install all dependencies using pip and requirements.txt 
    
    ```python
    pip3 install -r requirements.txt
    ```
    
5. Make sure you have your MySQL database running. On debian based systems you can check by 
    
    ```python
    sudo systemctl status mysqld
    ```
    
6. Make sure you have access and credentials to modify the database, enter them inside manage_db.py file.
    
    ```python
    dataBase = mysql.connector.connect(
        host= 'localhost',
        user= '<your - username>',
        passwd = '<your - mysql - password>',
    
    )
    ```
    
7. Then run this file
    
    ```python
    $python3 manage_db.py
    ```
    
8. Then set up this created database for django use
    
    ```python
    $python3 manage.py makemigrations client term_access
    $python manage.py migrate
    ```
    
9. Then set up administrator user account, you will need these creds when viewing dashboard.

```python
$python .\manage.py createsuperuser
Username (leave blank to use 'your-username'): 
Email address:
Password:
Password (again):
```

1. Before running the remote automatic website 

```python
$python3 manage.py runserver 0.0.0.0:8000
```

1. Now navigate to server folder and run  [server.py](http://server.py) 

```python
$pwd
#Cyethack-Assignment/server/

$python server.py
#ip:  127.0.0.1
#port 8080
#Server is listening for incoming connections.
```

1. If you navigate to Cyethack-Assignment/client/dist directory, you will find client.exe, which can be transferred to the client windows machine. This client needs to be run as administrator to work properly.
It asks for masters ip address and port it is listening on.
    
    ```python
    ENTER SERVER IP<MASTER- IP address>
    ENTER SERVER PORT<MASTER PORT>
    ```
    

### Features

- Multiple slaves can be connected simultaneously
- Checks with the slave machines every 5 mins
- Clean storage by automatically removing the data of the slave machine after it has closed the client.exe

### Examples

- DashBoard
- ![example 1](https://github.com/arhantbararia/Cyethack-Assignment/assets/61796574/38fd9f72-cf07-499f-9cfd-647a6b962937)

- Output of server.py
- ![example 2](https://github.com/arhantbararia/Cyethack-Assignment/assets/61796574/8075dfac-5762-48fd-a3b4-8593848809b3)

- Output of running client.exe
- ![example 3](https://github.com/arhantbararia/Cyethack-Assignment/assets/61796574/8ae5cdfd-c5a0-4bb5-a7f1-cd43d5d08e60)

- Output when a machine (slave) disconnects
- ![example 4](https://github.com/arhantbararia/Cyethack-Assignment/assets/61796574/f9644ca2-445f-4dc3-9bcc-61fc8d28525b)

- Dashboard for a specific machine
- ![example 5](https://github.com/arhantbararia/Cyethack-Assignment/assets/61796574/faacb7ff-74c1-419e-b8d0-d97ab23fd69f)

