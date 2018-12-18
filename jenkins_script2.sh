#!/bin/bash
source ./env/bin/activate
pip freeze
sudo -H pip install -r requirements.txt
cd inventoryproject
#python manage.py runserver
pytest --junit-xml=pytest_xml.xml
pip freeze
py.test --cov=inventory inventory/ --cov-report html --cov-report xml
deactivate
