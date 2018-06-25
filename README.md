# Django-Crime-Analytics-Web-App
A Django Based Crime Visualization and ML Application 

Visualization done using:

- Plotly

- FusionCharts

Machine learning done using a pretrained model


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




## Running on Heroku:

https://crimeanalyticsdjango.herokuapp.com/

### Staff user login

Username : Admin

Password: 12345six



