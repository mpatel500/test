pip install -r requirements.txt
cd inventoryproject
pytest --junit-xml=pytest_xml.xml
py.test --cov=inventory inventory/ --cov-report html --cov-report xml
