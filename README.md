# devsecops-pruebas-automatizadas

[![CI](https://github.com/0kmango/devsecops-pruebas-automatizadas/actions/workflows/ci.yml/badge.svg)](https://github.com/0kmango/devsecops-pruebas-automatizadas/actions/workflows/ci.yml)

Ejercicio de la **guía 3.2.3 (OCY1102 · EA 3 – Ciberseguridad en desarrollo de
software)**: partir de una aplicación mínima y agregarle las prácticas básicas
de un flujo DevSecOps, es decir, que **cada cambio se valide solo** antes de
llegar a `main`.

## ¿Qué contiene?

| Archivo | Rol |
| :--- | :--- |
| `app.py` | Aplicación base del ejercicio (solo biblioteca estándar). |
| `tests/test_app.py` | Pruebas automatizadas con `pytest` (sin red, deterministas). |
| `requirements.txt` | Dependencias de desarrollo (`pytest`, `pytest-cov`). |
| `Jenkinsfile` | Pipeline que prepara el entorno, valida sintaxis y ejecuta las pruebas. |
| `.github/workflows/ci.yml` | CI en GitHub Actions que replica esas validaciones en cada push y PR. |

## Ejecutar las pruebas en local

```bash
python3 -m venv .venv
. .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt
pytest -v                     # 4 pruebas, sin acceso a red
```

Con cobertura (opcional, para el informe):

```bash
pytest --cov=. --cov-report=term-missing
```

## Estados del flujo

1. **Validar sintaxis**: `python -m compileall -q app.py` — detecta errores de
   sintaxis en segundos.
2. **Pruebas automatizadas**: `pytest -v` — verifica el comportamiento real de
   la aplicación.
3. **Artefactos**: el `Jenkinsfile` deja `resultados/pruebas.xml`, revisable
   desde el build de Jenkins.

## Notas de seguridad del propio pipeline

- El workflow declara `permissions: contents: read`, es decir, el token de
  GitHub Actions solo puede leer el repositorio (principio de mínimo privilegio).
- No hay `secrets` en el código: la aplicación de ejemplo no necesita
  credenciales, así que no se exponen.
- Se bloquean builds concurrentes (`disableConcurrentBuilds`) para que dos
  ejecuciones no se pisen en el mismo workspace de Jenkins.
