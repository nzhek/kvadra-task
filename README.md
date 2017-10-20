Test task for Kvadra
========================

1. Setting virualenv
2. Cd to dir project and install virtualenv:
> Example: python -m venv testTask

3. Activate virtualenv:
> Example: testTask\Scripts\active

4.Database PostgresSql 9.4 (test password)
> name: nzhek_test
> login: postgres
> password: 123456

5. Make migrations db
> python manage.py makemigrations
> python manage.py migrate

6. Create superuser
> python manage.py createsuperuser

7. Install requirements
> pip3 install -r requirements.txt (Windows OS)
or install to manual

8. run project
> python manage.py runserver

