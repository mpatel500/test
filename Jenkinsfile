pipeline {
    agent any
	stages {
		stage (‘Checkout’) {
			steps {
				git "https://github.com/mpatel500/test.git"
				}
			}
		stage ('Install pip') {
			steps {
				sh "sudo apt-get install python-pip python-dev build-essential" 
				sh "sudo pip install --upgrade pip" 
				sh "sudo pip install --upgrade virtualenv"
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
