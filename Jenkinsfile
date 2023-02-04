pipeline {
    agent any

    stages {
        stage('Building') {
            steps {
                bat 'docker build -t my-flask-app .'
            }
        }
        stage('Running') {
            steps {
                bat 'docker run -d -p 5000:5000 ml_flask_app'
            }
        }
        stage('Testing') {
            steps {
                bat 'py -m pytest'
            }
        }
    }
}
