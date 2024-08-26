pipeline {
    agent any

    environment {
        WEATHER_API_KEY = credentials('WEATHER_API_KEY')  // Ensure this ID matches the credentials in Jenkins
    }

    stages {
        stage('Clean Workspace') {
            steps {
                // Clean the workspace before starting
                cleanWs()
            }
        }

        stage('Clone Repository') {
            steps {
                // Clone the specified branch from your Git repository
                git branch: 'feature/jenkins', credentialsId: 'GITHUB_PAT', url: 'https://github.com/KunalBhoyar/Weather_update.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Build the Docker image using Docker Compose
                    sh 'docker-compose build'
                }
            }
        }

        stage('Run Application') {
            steps {
                script {
                    // Run the application using Docker Compose
                    sh 'docker-compose up -d'
                }
            }
        }
    }

    post {
        always {
            // Clean up Docker containers after the pipeline runs
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
