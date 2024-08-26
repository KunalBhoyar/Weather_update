pipeline {
    agent any

    parameters {
        string(name: 'BRANCH_NAME', defaultValue: 'main', description: 'Specify the Git branch to build')
    }

    environment {
        WEATHER_API_KEY = credentials('WEATHER_API_KEY')
    }

    stages {
        stage('Clean Workspace') {
            steps {
                cleanWs()  // Clean the workspace before starting
            }
        }

        stage('Clone Repository') {
            steps {
                // Use the parameterized branch name
                git branch: "${params.BRANCH_NAME}", credentialsId: 'GITHUB_PAT', url: 'https://github.com/KunalBhoyar/Weather_update.git'
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
