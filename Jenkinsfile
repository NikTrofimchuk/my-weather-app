pipeline {
    agent any

    triggers {
        pollSCM('H/2 * * * *') // каждые 2 минуты
    }

    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    dockerImage = docker.build("weather-app")
                }
            }
        }

        stage('Docker Push') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'docker-hub-creds', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    sh """
                    echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
                    docker tag weather-app $DOCKER_USER/weather-app
                    docker push $DOCKER_USER/weather-app
                    """
                }
            }
        }

        stage('Deploy on VM') {
            steps {
                sshagent(credentials: ['ansible-ssh-key']) {
                    sh 'ansible-playbook -i Ansible\inventory.ini Ansible\deploy.yml'
                }
            }
        }
    } 
}