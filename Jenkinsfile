pipeline {
    agent any  // This specifies that the pipeline can run on any available agent

     environment {
        DOCKER_HOST = "tcp://socat-proxy:2375"  // Use port 2375, which is working
        DOCKER_TLS_VERIFY = "0"  // Disable TLS (forces HTTP)
        DOCKER_IMAGE = "weather-app"
    }

    stages {
    stage('Build') {
        steps {
            script {
                docker.build("${env.DOCKER_IMAGE}")
            }
        }
    }


        stage('Test') {
            steps {
                // Here you can add steps to run tests
                echo 'Running tests...'
                // For example: sh 'docker run ${env.DOCKER_IMAGE} pytest'
            }
        }

        stage('Deploy') {
            steps {
                // Run the Docker container
                echo 'Deploying the application...'
                sh "docker run -d -p 5000:5000 ${env.DOCKER_IMAGE}"
            }
        }
    }

    post {
        // Define post-build actions
        always {
            echo 'This will always run'
        }
        success {
            echo 'Build was a success!'
            // Actions to perform on success
        }
        failure {
            echo 'Build failed!'
            // Actions to perform on failure
        }
    }
}




