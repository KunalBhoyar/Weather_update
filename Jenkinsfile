pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                script {
                    docker.withServer('tcp://172.19.0.2:2375', '') {
                        docker.build('weather-app')
                    }
                }
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests...'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying the application...'
                sh "docker run -d -p 5000:5000 weather-app"
            }
        }
    }
}
