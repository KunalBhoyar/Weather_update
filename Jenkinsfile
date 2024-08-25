pipeline {
    agent any

    environment {
        // Securely fetch the API key from Jenkins credentials store
        WEATHER_API_KEY = credentials('WEATHER_API_KEY')  // This assumes you stored the key in Jenkins credentials with ID 'WEATHER_API_KEY'
    }

    stages {
        stage('Clone Repository') {
            steps {
                // Clone the repository from Git
                git branch: 'main', url: 'https://github.com/your-repo/weather-app.git'  // Replace with your actual repository URL and branch
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
                    // Run the Docker containers in detached mode
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
