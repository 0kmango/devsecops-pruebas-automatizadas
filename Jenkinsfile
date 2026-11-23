// Jenkinsfile - Pipeline con validaciones reales (guía 3.2.3, OCY1102)
//
// Antes este pipeline solo ejecutaba `echo`, así que un cambio roto seguía
// dando build verde. Ahora prepara un entorno virtual, valida la sintaxis del
// código y ejecuta la suite de pruebas automatizadas: si algo falla, el
// pipeline falla.
pipeline {
    agent any

    options {
        timestamps()
        disableConcurrentBuilds()
        skipDefaultCheckout(true)
    }

    stages {
        stage('Clonar código') {
            steps {
                checkout scm
            }
        }

        stage('Preparar entorno') {
            steps {
                sh 'python3 -m venv .venv'
                sh '. .venv/bin/activate && python -m pip install --upgrade pip'
                sh '. .venv/bin/activate && pip install -r requirements.txt'
            }
        }

        stage('Validar sintaxis') {
            steps {
                sh '. .venv/bin/activate && python -m compileall -q app.py'
            }
        }

        stage('Pruebas automatizadas') {
            steps {
                sh 'mkdir -p resultados'
                sh '. .venv/bin/activate && pytest -v --junitxml=resultados/pruebas.xml'
            }
        }
    }

    post {
        always {
            // El reporte XML queda archivado para revisarlo desde Jenkins
            // (pestaña de artefactos del build).
            archiveArtifacts artifacts: 'resultados/**', allowEmptyArchive: true
        }
        success {
            echo 'Pipeline OK: sintaxis y pruebas automatizadas superadas.'
        }
        failure {
            echo 'Pipeline FALLÓ: revisa la salida de pytest en los artefactos del build.'
        }
    }
}
