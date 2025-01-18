Lezapi Application

Prerequisites:
- Python (3.8 or newer)

Getting Started:

1. **Set up your virtual environment**

In the project directory, please run:

For Unix or MacOS:
```
python3 -m venv env
source env/bin/activate
```

For Windows:
```
py -m venv env
.\env\Scripts\activate
```

This will create a new virtual environment and activate it.

2. Install Django

While in the activated environment, install Django with pip:

```
pip install django
```

This command will install Django.

3. Apply Migrations

Navigate to the Django project directory, the one with the `manage.py` file, and run the following command:

```
python manage.py makemigrations
python manage.py migrate
```

These commands will apply the migrations.

4. Create admin superuser

To access the admin interface, we need a user with admin privileges:

```
python manage.py createsuperuser
```

Follow command prompts to set the username and password.

5. Run the development server

Finally, you can run the development server with:

```
python manage.py runserver
```

You should see output on the command line with the address of the development server, likely http://127.0.0.1:8000/

Now, with your server running, visit http://127.0.0.1:8000/admin in your web browser. You should see the admin interface login page. 

After logging in with your superuser credentials, you can create, update, and delete records in your database models.

(Note: The commands above assume your manage.py file is in the current directory. Adjust the file path as needed.)