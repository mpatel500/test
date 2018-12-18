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
				sh "python3 -m venv ./env"
				sh "pwd"
				sh "whoami"
				sh "pip freeze"
				sh "sudo bash ./jenkins_script2.sh"
				sh "deactivate"
				}
			}
		stage ('Publish Reports') {
			steps {
				sh "ls"
				junit 'inventoryproject/pytest_xml.xml'
				publishHTML([allowMissing: false, alwaysLinkToLastBuild: false, keepAll: false, reportDir: 'inventoryproject/htmlcov', reportFiles: 'index.html', reportName: 'HTML Report', reportTitles: ''])
				cobertura autoUpdateHealth: false, autoUpdateStability: false, coberturaReportFile: 'inventoryproject/coverage.xml', conditionalCoverageTargets: '70, 0, 0', failUnhealthy: false, failUnstable: false, lineCoverageTargets: '80, 0, 0', maxNumberOfBuilds: 0, methodCoverageTargets: '80, 0, 0', onlyStable: false, sourceEncoding: 'ASCII', zoomCoverageChart: false
				}
			}
		}
}
