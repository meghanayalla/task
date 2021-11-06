## Car Rental GET API

It is a flask based search API that fetches the data of top 3 cars nearest to the user's location. It uses the data stored in a MongoDB database. 
We have used  cloud based database named MongoDB  Atlas for ease of usage and easy deployment across systems.

### Technologies Used

 - Python
 - Flask
 - MongoDB
 - Minor dependencies can be found in the requirements.txt
### Installation (without docker)
 - To use the API ensure that python3 is installed on the system
 - Create a virtual environment to isolated your system from global changes.
 ```
pip install virtualenv
virtualenv -p python3 venv
source venv/bin/activate
```
- Next, install the project dependencies.
```
pip install -r requirements.txt
``` 
- Finally, to run the app,
```
python app.py
```

The app by default runs on local host. It can be accessed using any web browser at  **http://127.0.0.1:5000/** or **http://localhost:5000/**
You should see Hello! if the app runs successfully.
### Usage
- The get method of the API can be accessed at:
`/get/`
- In order to use the search API we need to provide the coordinates of the user as URL parameters.
The way to do so is specified below:
`/get/<longitude>/<latitude>/`

- For example:
To fetch the results for latitude =-17.686 , longitude = 83.2185
The URL should be of the form (considering local host)
`http://localhost:5000/get/83.2185/-17.686`

Alternatively, you can also use Postman to test the API

---
**NOTE**

- Latitudes and Longitudes are float values and use of integer values will throw an error.
- For example : `/get/40/50` will throw an error
    Instead, use `/get/40.0/50.0`
---

### Installation using docker
Docker makes it easier to execute and install all the dependencies required for the project in one single command
To run the app, 


 - You need to have Docker Compose installed on your system. Docker Compose is included in
[Docker Desktop](https://www.docker.com/products/docker-desktop)
for Windows.
 -  Download all the files in the repository and save them in a folder. 
 - Open PowerShell in the directory
 - Finally run, ` docker compose up` and Compose will start and run the entire app.
 -  The API can be used in a similar way described above

 

