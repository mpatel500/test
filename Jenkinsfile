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
				sh "sudo bash ./wont_work_either_script.sh"
				sh "sudo bash ./jenkins_script.sh"
				}
			}
		}
}
