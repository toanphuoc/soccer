# soccer

I. Installation

	1. Install python(recommend python 3.x) at: 
		https://www.python.org/

	2. Download and install pip latest version: 
		https://pypi.python.org/pypi/pip
		
		python get-pip.py
		
	3. Install django framework: 
		https://www.djangoproject.com/

		pip install Django==1.9.5
		
	4. Install django-rest-framework: 
		http://www.django-rest-framework.org/#installation

		pip install djangorestframework
		
		pip install markdown
		
		pip install django-filters

	5. Download and install psycopg2 at: 
		http://www.stickpeople.com/projects/python/win-psycopg/

II. Migration database and run server
	
	1. Migration database

		python manage.py migrate

	2. Run server

		python manage.py runserver

III. Create admin user:

	-	First we’ll need to create a user who can login to the admin site. Run the following command:
		$ python manage.py createsuperuser
	-	Enter your desired username and press enter.
		Username: admin
	-	You will then be prompted for your desired email address:
		Email address: admin@example.com
	-	The final step is to enter your password. You will be asked to enter your password twice, the second time as a confirmation of the first.
		Password: **********
		Password (again): *********
		Superuser created successfully.

