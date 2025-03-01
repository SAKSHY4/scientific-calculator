pipeline {
    agent any
    environment {
        DOCKER_IMAGE_NAME = 'scientific-calculator'
        GITHUB_REPO_URL = 'https://github.com/SAKSHY4/scientific-calculator.git'
    }
    stages {
        stage('Checkout') {
            steps {
                script {
                    git branch: 'master', url: "${GITHUB_REPO_URL}"
                }
            }
        }
        stage('Install Dependencies') {
            steps {
                script {
                    sh '''
                        python3 -m venv venv
                        . venv/bin/activate
                        pip install --upgrade pip
                        pip install -r requirements.txt
                    '''
                }
            }
        }
        stage('Run Tests') {
            steps {
                script {
                    // Activate the same virtual environment for tests
                    sh '''
                        . venv/bin/activate
                        pytest test_calculator.py
                    '''
                }
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("${DOCKER_IMAGE_NAME}", '.')
                }
            }
        }
        stage('Push Docker Image') {
            steps {
                script {
                    docker.withRegistry('', 'DockerHubCred') {
                        sh "docker tag ${DOCKER_IMAGE_NAME} sakshya4/scientific-calculator:0.0.1"
                        sh "docker push sakshya4/scientific-calculator"
                    }
                }
            }
        }
        stage('Run Ansible Playbook') {
            steps {
                script {
                    ansiblePlaybook(
                        playbook: 'deploy.yml',
                        inventory: 'inventory'
                    )
                }
            }
        }
    }
}
