pip install -r requirements.txt
cd inventoryproject
pytest --junit-xml=pytest_xml.xml
coverage run pytest.ini
coverage report -m
coverage xml -o coverage_report.xml
coverage html -d coverage


