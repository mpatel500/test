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
				sh "sudo ./jenkins_script"
				}
			}
		}
}
