pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                script {
                    docker.build('weather-app')
                }
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests...'
                // Add any test steps here, if necessary
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying the application...'
                sh "docker run -d -p 5000:5000 weather-app"
            }
        }
    }

    post {
        always {
            echo 'This will always run'
        }
        success {
            echo 'Build was a success!'
        }
        failure {
            echo 'Build failed!'
        }
    }
}
