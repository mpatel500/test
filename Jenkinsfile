pipeline {
    agent any
	stages {
		stage (‘Checkout’) {
			steps {
				git "https://github.com/mpatel500/test.git"
				}
			}
		stage (‘Build’) {
			steps {
				sh "pwd"
				sh "whoami"
				sh "sudo bash ./jenkins_script2.sh"
				}
			}
		stage ('Publish Reports') {
			steps {
				sh "ls"
				junit 'inventoryproject/pytest_xml.xml'
				publishHTML([allowMissing: false, alwaysLinkToLastBuild: false, keepAll: false, reportDir: 'htmlcov', reportFiles: 'index.html', reportName: 'HTML Report', reportTitles: ''])
				}
			}
		}
}
