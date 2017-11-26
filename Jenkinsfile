pipeline {
    agent any
    stages {
        stage ('Checkout') {
            steps {
                checkout scm
            }
        }
        stage ('Prepare Environment') {
            steps {
                sh "pip install -r requirements.txt"
            }
        }
        stage ('Test') {
            steps {
                sh "python diablo2/manage.py test"
            }
        }
    }
}
