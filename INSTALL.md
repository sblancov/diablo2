First of all, clone this repository.

    git clone < this-repository >

Then execute these commands to start a Django HTTP server (only for test
purposes):

    python manage.py makemigrations
    python manage.py migrate
    python manage.py createsuperuser
    python manage.py runserver 0.0.0.0:8081

Now type 'localhost:8081' in your browser and play!
