pip install -r requirements.txt
cd inventoryproject
pytest --junit-xml=pytest_xml.xml
py.test --cov=test
