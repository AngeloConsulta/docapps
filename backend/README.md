This is an Django Simple Sign Up and Login

Must sign Up the Email Registration 
Then go to login section
1. SetUp Project
    *Create New Project django-admin startproject DocSys (DocSys)
    *Create new app python manage.py startapp core
    *Install the apps in setting.py
    *Configure Templates  import os[[os.path.join(BASE_DIR, 'templates')]]
    *Configure Static and Media Files in setting.py and urls.py 
        *path('', index, name='home'), the video did not consider this to put
    *Create a new view, urls and template then runserver
    *Configure template inheritance and partials

2. Configure Admin page, Superuser and Jazzmin
    *Install Jazzmin(pip install django-jazzmin)
    *Add jazzmin in INSTALLED_APPS
    *Add Jazzmin Config coden in Settings.py
    *Create Superuser
    Before begin with it, Type this in terminal python manage.py migrate then next is python manage.py createsuperuser
    *Login to Admin Section

3. Custom the User Models 
    *Create new apps Userauths or Signup
    *Install apps in settings.py
    *Create custom class User(AbstractUsers): in models.py
4. User Registration System
    *Create new form in form.py
    *Write to register def RegisterView(request) user
    *Configure template to show form
    *Login to Website from Frontend

5. User Login System 
    *Write view to login def LoginView(request);
    *Configure template to grab input field
    *Login to Website from Frontend 

6. User Logout System
    * Write view def LogoutView(request); to Logout a user
    *Configure URL
    *Test the Feature
 # This is Jjason handled by Angelo


    
