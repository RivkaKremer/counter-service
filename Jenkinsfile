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
    }
    post {
        success{
            script{
                println("CI Pipeline Succeed, Now CD Should Be Automatically Triggered By Flux...")
            }
        }
        failure{
            script{
                println("CI Pipeline Failed, Please Check The Errors...")
            }
        }
    }
}
