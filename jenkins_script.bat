pip install -r requirements.txt
cd inventoryproject
pytest --junit-xml=pytest_xml.xml
cd ..
py.test --cov=test
