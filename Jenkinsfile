pipeline {
    agent any
    stages {
        stage('Say hello') {
            steps {
                echo 'Hello pipeline!'
            }
        }
        stage ('Checkout') {
            steps {
                checkout scm
            }
        }
    }
}
