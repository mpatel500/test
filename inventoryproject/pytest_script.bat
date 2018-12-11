call mkvirtualenv jenkins_test
pip install pytest
pytest --junit-xml=test_xml.xml
call deactivate jenkins_test
call rmvirtualenv jenkins_test