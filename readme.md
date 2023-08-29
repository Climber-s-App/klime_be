run:

pip install -r requirements.txt
python3 -m venv .venv
. .venv/bin/activate
python manage.py makemigrations
python manage.py migrate
