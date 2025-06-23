pipeline{
    agent any

    environment {
        VENV_DIR = 'venv'
        GCP_PROJECT = ""
        GCLOUD_PATH = "/var/jenkins_home/google-cloud-sdk/bin"
    }

    stages{
        stage('Cloning Github repo to Jenkins'){
            steps{
                script{
                    echo 'Cloning Github repo to Jenkins............'
                    checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'GitHub_Token', url: 'https://github.com/Nopass0y/MLOps-course-project-1.git']])
                }
            }
        }
    }
}