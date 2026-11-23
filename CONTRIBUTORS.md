# Colaboradores

| Cuenta | Rol en el proyecto |
| :--- | :--- |
| [@0kmango](https://github.com/0kmango) | Autora del código de ejemplo (`app.py`), de la suite de pruebas (`tests/`) y de los pipelines de Jenkins y GitHub Actions |
| [@MartinaNorambuena](https://github.com/MartinaNorambuena) | Coautoría de la documentación y revisión del flujo de integración continua |

Este repositorio es un ejercicio de la **guía 3.2.3 (OCY1102 · EA 3 —
Ciberseguridad en desarrollo de software)**. La coautoría se registra con la
directiva [`Co-authored-by`](https://docs.github.com/en/pull-requests/committing-changes-to-your-project/creating-and-editing-commits/creating-a-commit-with-multiple-authors)
de Git, de modo que ambas cuentas quedan acreditadas en el historial.

## Cómo reproducir el flujo completo

```bash
# 1. Clonar el repositorio
git clone https://github.com/0kmango/devsecops-pruebas-automatizadas.git
cd devsecops-pruebas-automatizadas

# 2. Preparar el entorno
python3 -m venv .venv
. .venv/bin/activate                      # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# 3. Validar sintaxis y ejecutar las pruebas
python -m compileall -q app.py
pytest -q                                 # 4 pruebas
```

En Jenkins: *New Item → Pipeline → Pipeline script from SCM*, rama `*/main` y
`Jenkinsfile` como ruta del script. El `Jenkinsfile` hace exactamente los mismos
pasos que el comando anterior y archiva `resultados/pruebas.xml`.

En GitHub Actions no hay que configurar nada: `.github/workflows/ci.yml` corre
en cada `push` y en cada *pull request*.
