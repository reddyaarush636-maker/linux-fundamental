2. Lists  =  A list stores multiple values in one variable
---------------------------------
vim list.py
servers = ["web1", "web2", "web3"]

print(servers)

OUTPUT = ['web1', 'web2', 'web3']

3. Dictionaries   = A dictionary stores data as
--------------------
vim dic.py
server = {
    "name": "web-server",
    "ip": "192.168.1.10",
    "port": 80,
    "status": "running"
}

print(server["name"])
print(server["ip"])
print(server["status"])

4. if / else   = if/else is used to make decisions
-----------------------------------------------------------
vim if.py
status = "running"

if status == "running":
    print("Server is UP")
else:
    print("Server is DOWN")
  ***********************************

cpu = 90

if cpu > 80:
    print("WARNING: CPU is high")
else:
    print("CPU is normal")


5. Loops  = Loops are used to repeat something
------------------------------------------------------
vim for.py
servers = ["web1", "web2", "web3"]

for server in servers:
    print("Checking", server)

***********************************************************
servers = ["web1", "web2", "web3"]

for server in servers:
    print("Restarting", server)

while loop  = Keep doing something while the condition is true
---------------------------------------------------------------------
count = 1

while count <= 5:
    print(count)
    count = count + 1

6. Functions = A function is a reusable block of code
-----------------------------------------------------------
vim fun.py
def deploy(server):
    print("Deploying application to", server)

deploy("web1")
deploy("web2")

7. Files = Python can read and write files
---------------------------------------------------
vim file.py
file = open("server.txt", "w")

file.write("web1\n")
file.write("web2\n")
file.write("web3\n")

file.close()

**********************************************
with open("server.txt", "w") as file:
    file.write("web1\n")
    file.write("web2\n")


8. Exceptions = Exceptions are errors that happen while the program is running
-------------------------------------------------------------------------------------
number = int(input("Enter number: "))

print(100 / number)

**********************************************************888
try:
    number = int(input("Enter number: "))
    result = 100 / number
    print(result)

except ZeroDivisionError:
    print("Cannot divide by zero")

except ValueError:
    print("Please enter a number")

9. Modules  = A module is basically a Python file/library containing useful code that you can use in another program
-------------------------------------------------------------------------------------------------------------------------
vim module.py
import os

print(os.getcwd())

*********************************************
  import datetime

today = datetime.datetime.now()

print(today)


10. Requests = requests is commonly used to make HTTP/API requests
-----------------------------------------------------------------------
vim req.py
import requests

response = requests.get("https://api.github.com")

print(response.status_code)

./req.py

OUTPUT 200 = 200 meanse request is success 
***********************************************************
Common HTTP codes:
200 → Success
201 → Created
400 → Bad request
401 → Unauthorized
403 → Forbidden
404 → Not found
500 → Server error

Python can communicate with:
-------------------------------------
GitHub API
AWS APIs
Kubernetes APIs
Jenkins APIs
Docker APIs
Monitoring systems


11. JSON = JSON is a common format for sending and receiving data through APIs
---------------------------------------------------------------------------------
json
{
    "name": "web-server",
    "ip": "192.168.1.10",
    "port": 80,
    "status": "running"

python

  server = {
    "name": "web-server",
    "ip": "192.168.1.10",
    "port": 80
}
}


12. Python + API + JSON — Real Example
---------------------------------------------------------
This is where these concepts start becoming real DevOps.

vim demo.py
import requests

url = "https://api.github.com"

response = requests.get(url)

print(response.status_code)

data = response.json()

print(data)

********************************************************
  import requests

servers = [
    "https://example.com",
    "https://github.com"
]

def check_server(url):

    try:
        response = requests.get(url, timeout=5)

        if response.status_code == 200:
            print(url, "→ UP")
        else:
            print(url, "→ Problem:", response.status_code)

    except requests.exceptions.RequestException:
        print(url, "→ DOWN")


for server in servers:
    check_server(server)











