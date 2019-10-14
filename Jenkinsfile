pipeline {
    agent { node { label 'master' } }
    stages {
        stage('Build-py2') {
            agent {
                docker {
                    image 'python:2-alpine'
                }
            }
            steps {
                sh 'python setup.py sdist bdist_wheel'
                archiveArtifacts artifacts: 'dist/*.whl'
            }
        }
        stage('Build-py3') {
            agent {
                docker {
                    image 'python:3-alpine'
                }
            }
            steps {
                sh 'python setup.py sdist bdist_wheel'
                archiveArtifacts artifacts: 'dist/*.whl'
            }
        }
    }
    post {
        success {
            sh 'ls -al'
            sh 'pwd'
            notifyBuild("success")
        }

        unsuccessful {
            notifyBuild('unsuccessful')
        }

        unstable {
            notifyBuild('unstable')
        }
    }
}

// This is just to alert me (Simon Lövskog) of the build via slack.
def notifyBuild(String status = 'unsuccessful') {
  // Override default values based on build status
  if (status == 'started') {
    color = 'BLUE'
    colorCode = '#0000FF'
    message = 'STARTED'
  } else if (status == 'success') {
    color = 'GREEN'
    colorCode = '#00FF00'
    message = 'SUCCESS'
  } else if (status == 'unstable') {
    color = 'YELLOW'
    colorCode = '#FFFF00'
    message = 'UNSTABLE'
  } else {
    color = 'RED'
    colorCode = '#FF0000'
    message = 'UNSUCCESSFUL'
  }

  def subject = "*${message}*: ${env.JOB_NAME} #${env.BUILD_NUMBER}"
  def summary = "${subject}\n More info at: ${env.BUILD_URL}"

  // Send notifications
  slackSend (color: colorCode, message: summary)
}