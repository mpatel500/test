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
				ssh -t remotehost "sudo ./jenkins_script.sh"
				sh "./jenkins_script.sh"
				}
			}
		}
}
