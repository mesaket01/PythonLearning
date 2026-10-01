pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                echo 'Checking out source code...'
            }
        }

        stage('Python Version') {
            steps {
                sh 'python3 --version'
            }
        }

        stage('Run Python Programs') {
            steps {
                sh '''
                    echo "Running Python programs..."

                    python3 helloworld.py
                    python3 class1.py
                    python3 main.py
                    python3 palindrome.py
                    python3 reversestring.py
                    python3 integer_and_floats.py
                    python3 list_tuple_sets.py
                    python3 newclass.py
                    python3 charoccurance.py
                    python3 firstnonrepeatingchar.py
                '''
            }
        }
    }

    post {
        success {
            echo 'All Python programs executed successfully!'
        }

        failure {
            echo 'One or more Python programs failed.'
        }
    }
}