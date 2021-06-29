def DAY_TO_KEEP_STR = '14'

def NUM_TO_KEEP_STR = '42'

pipeline{
    agent {
        label 'jenkins-slave'
    }
    options{
        buildDiscarder(logRotator(daysToKeepStr: DAY_TO_KEEP_STR, numToKeepStr: NUM_TO_KEEP_STR))
        timestamps()
    }
    environment {
        version = 'latest'
        registry = '630943284793.dkr.ecr.us-west-1.amazonaws.com/counter-service'
        registryCredential = 'aws-creds'
        dockerImage = ''
    }
    stages{
        stage('Build Image'){
            steps{
                script {
                    dir('app'){
                        dockerImage = docker.build registry
                    }
                }
            }
        }
        stage('Publish image') {
            steps{
                script{
                    docker.withRegistry("https://" + registry, "ecr:us-west-1:" + registryCredential) {
                        dockerImage.push("0.0.${env.BUILD_NUMBER}")
                        dockerImage.push('latest')
                    }
                }
            }
        }
        stage('Deploy image'){
            steps{
                script{
                    sh """
                        sed -i "s/630943284793.dkr.ecr.us-west-1.amazonaws.com\\/counter-service:0.0.[0-9]*/630943284793.dkr.ecr.us-west-1.amazonaws.com\\/counter-service:0.0.${env.BUILD_NUMBER}/g" k8s-app-components/counter-service.yaml
                        echo 1
                        git add k8s-app-components/counter-service.yaml
                        echo 2
                        git commit -m "Updated version to 0.0.${env.BUILD_NUMBER}"
                        echo 3
                        git push origin $GIT_BRANCH
                    """
                }
            }
        }
    }
//    post {
//        always {
//
//        }
//        success{
//
//        }
//        failure{
//
//        }
//    }
}
