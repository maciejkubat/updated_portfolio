pipeline {
    agent any

    environment {
        DOCKER_REGISTRY = 'docker.io'
        DOCKER_IMAGE_NAME = 'treku2/portfolio'
        DOCKER_IMAGE_TAG = "${BUILD_NUMBER}"
        DOCKER_CREDENTIALS = credentials('docker_hub')
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out code...'
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                echo "Building Docker image: ${DOCKER_IMAGE_NAME}:${DOCKER_IMAGE_TAG}"
                sh '''
                    docker build -t ${DOCKER_IMAGE_NAME}:${DOCKER_IMAGE_TAG} .
                    docker tag ${DOCKER_IMAGE_NAME}:${DOCKER_IMAGE_TAG} ${DOCKER_IMAGE_NAME}:latest
                '''
            }
        }

        stage('Approval for Docker Hub Push') {
            steps {
                echo "Docker image built successfully!"
                echo "Image tags:"
                echo "  - ${DOCKER_IMAGE_NAME}:${DOCKER_IMAGE_TAG}"
                echo "  - ${DOCKER_IMAGE_NAME}:latest"
                
                input(
                    message: "Do you want to push this image to Docker Hub?",
                    ok: 'Push',
                    submitter: null
                )
            }
        }

        stage('Push to Docker Hub') {
            steps {
                echo 'Logging in to Docker Hub...'
                sh '''
                    echo "${DOCKER_CREDENTIALS_PSW}" | docker login -u "${DOCKER_CREDENTIALS_USR}" --password-stdin
                '''
                
                echo "Pushing image to Docker Hub..."
                sh '''
                    docker push ${DOCKER_IMAGE_NAME}:${DOCKER_IMAGE_TAG}
                    docker push ${DOCKER_IMAGE_NAME}:latest
                '''
                
                echo 'Logging out from Docker Hub...'
                sh 'docker logout'
            }
        }
    }

    post {
        always {
            echo 'Pipeline execution completed.'
        }
        success {
            echo "✓ Docker image pushed successfully!"
        }
        failure {
            echo "✗ Pipeline failed. Check logs for details."
        }
        aborted {
            echo "Pipeline was aborted by user or system."
        }
    }
}
