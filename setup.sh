
# establishes environment file
python -m venv .venv

# activates the virtual environment
. .venv/bin/activate

# installs dependencies for app from text file (into .venv)
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# # Start the Django development server
#   python manage.py runserver 0.0.0.0:$PORT