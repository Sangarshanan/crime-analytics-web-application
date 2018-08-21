# Django-Crime-Analytics-Web-App
A Django Based Crime Visualization and ML Application 

Visualization done with the help:

- Plotly

- FusionCharts

Machine learning done using a pretrained bayesian model


## Running in your local system:

Clone the repository and navigate to the folder

Open your shell and install pip (If you don't have it)

Now, install all the requirements using the below command

```
pip install -r requirements.txt
```

Now create your own Admin/Superuser

```
python manage.py createsuperuser
```

You can now login using your credentials, but before logging in we need be migrate our database content

```
python manage.py makemigrations

python manage.py migrate
```
To host the application on your localhost

```
python manage.py runserver
```

To Update the database contents run the python files
``` 
python import.py 
python import1.py
```  

Running these two python codes would insert all csv contents to the Sqlite database


## Running on Heroku:

https://crimeanalyticsdjango.herokuapp.com/

### Staff user login

Username : Admin

Password : 12345six



