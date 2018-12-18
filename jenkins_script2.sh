#!/bin/bash
source ./env/bin/activate
pip freeze
pip install -r requirements.txt
sudo -H pip install -r requirements.txt
cd inventoryproject
python manage.py runserver
pytest --junit-xml=pytest_xml.xml
py.test --cov=inventory inventory/ --cov-report html --cov-report xml
