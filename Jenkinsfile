pipeline {
    agent { node { label 'master' } }
    environment {
      pypiCreds = credentials('pypi-simoncircle')
    }
    stages {
        stage('Build-py2') {
            agent {
                docker {
                    image 'python:2-alpine'
                }
            }
            steps {
                sh 'python setup.py sdist bdist_wheel'

                sh 'pip install twine'
                sh 'twine upload -u $pypiCreds_USR -p $pypiCreds_PSW dist/*'

                archiveArtifacts artifacts: 'dist/*.whl', fingerprint: true
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

                sh 'pip install twine'
                sh 'twine upload -u $pypiCreds_USR -p $pypiCreds_PSW dist/*'

                archiveArtifacts artifacts: 'dist/*.whl', fingerprint: true
            }
        }
    }
    post {
        success {
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