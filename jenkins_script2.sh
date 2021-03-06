#!/bin/bash
source ./env/bin/activate
echo "PIP FREEZE BEFORE REQUIREMENTS.TXT IS INSTALLED"
pip freeze
sudo -H pip install -r requirements.txt
echo "PIP FREEZE AFTER REQUIREMENTS.TXT IS INSTALLED"
pip freeze
cd inventoryproject
#python manage.py runserver
pytest --junit-xml=pytest_xml.xml
echo "PYLINT CHECKING ERRORS OF PROJECT"
pylint -f parseable /inventory | tee pylint.out
py.test --cov=inventory inventory/ --cov-report html --cov-report xml --cov-fail-under=100
deactivate
