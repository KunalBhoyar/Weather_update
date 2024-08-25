pipeline {
    agent any

    environment {
        WEATHER_API_KEY = credentials('WEATHER_API_KEY')  // Make sure this matches the exact ID in Jenkins
    }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'feature/jenkins', credentialsId: 'GITHUB_PAT', url: 'https://github.com/KunalBhoyar/Weather_update.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh 'docker-compose build'
                }
            }
        }

        stage('Run Application') {
            steps {
                script {
                    sh 'docker-compose up -d'
                }
            }
        }
    }

    post {
        always {
            echo 'Cleaning up Docker containers...'
            sh 'docker-compose down'
        }
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed. Please check the logs.'
        }
    }
}
