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
                bat 'docker run -d -P ml_flask_app'
            }
        }
        stage('Testing') {
            steps {
                bat 'py -m pip install -r requirements.txt'
                bat 'py -m pytest'
            }
        }
    }
}
