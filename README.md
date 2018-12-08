To run project:

create virtual environment:
mkvirtualenv inventoryenv 

download requirements:
pip install -r requirements.txt 

To make migrations:
python manage.py make migrations 

To migrate:
python manage.py migrate 

To run the server: 
python manage.py runserver 

To close virtual enviornment:
deactivate 

To populate db with objects:
python manage.py shell
exec(open('sample_data.py').read())


