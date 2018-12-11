pip install -r requirements.txt
cd inventoryproject
pytest --junit-xml=pytest_xml.xml
junit 'pytest_xml.xml'
