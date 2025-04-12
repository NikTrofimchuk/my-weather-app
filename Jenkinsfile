pipeline {
    agent any

    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    dockerImage = docker.build("weather-app")
                }
            }
        }
    }

    stage('Push to Docker Hub') {
            steps {
                withDockerRegistry([credentialsId: 'docker-hub-creds', url: '']) {
                    script {
                        dockerImage.push('latest')
                    }
                }
            }
        }

    stage('Deploy with Ansible') {
        steps {
            sh 'ansible-playbook -i ansible/inventory.ini ansible/deploy.yml'
        }
    }
}
