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
				sh "sudo easy_install pip"
				sh "pwd"
				sh "whoami"
				sh "sudo bash ./jenkins_script.sh"
				}
			}
		}
}
