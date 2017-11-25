install:
	pip install -r requirements.txt

init:
	python diablo2/manage.py makemigrations
	python diablo2/manage.py migrate
	python diablo2/manage.py createsuperuser
