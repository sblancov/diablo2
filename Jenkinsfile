pipeline {
    agent any
    stages {
        stage ('Checkout') {
            steps {
                checkout scm
            }
        }
        stage ('Test') {
            steps {
                sh "python diablo2/manage.py test"
            }
        }
    }
}
