pipeline {
    agent any

    stages {
        stage('Build Docker Image') {
            steps {
                echo "Build Docker Image"
                bat 'docker build -t pythonflaskapp:v1 .'
            }
        }

        stage('Docker Login') {
            steps {
                echo "Docker Login"
                bat 'docker login -u sreeja20082004 -p Sreeja@12'
            }
        }

        stage('Push Docker Image to Docker Hub') {
            steps {
                echo "Push Docker Image to Docker Hub"
                bat 'docker tag pythonflaskapp:v1 sreeja20082004/sample:v1'
                bat 'docker push sreeja20082004/sample:v1 '
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                echo "Deploying to Kubernetes cluster"

                // ✅ Add kubeconfig environment variable
                bat '''
                set KUBECONFIG=C:\Users\vr_ma\.kube\config
                kubectl cluster-info
                kubectl apply -f deployment.yaml
                kubectl apply -f service.yaml
                '''
            }
        }
    }

    post {
        success {
            echo "Pipeline completed successfully!"
        }
        failure {
            echo "Pipeline failed. Please check the logs."
        }
    }
}
