"""Pruebas automatizadas para ``app.py`` (guía 3.2.3 · EA 3).

Objetivos de estas pruebas:

* Verificar el comportamiento observable de la aplicación (salida en
  ``stdout``) sin depender de la red ni de servicios externos.
* Ser rápidas y deterministas, para que puedan ejecutarse tanto en Jenkins
  como en GitHub Actions en cada push.
* Servir como ejemplo mínimo de "prueba automatizada" dentro del ejercicio
  de DevSecOps: si alguien rompe ``app.py``, el pipeline falla.

Ejecución local::

    pytest -v
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import app

RAIZ = Path(__file__).resolve().parent.parent
MENSAJE_ESPERADO = "Aplicación de ejemplo"


def test_main_imprime_el_mensaje_esperado(capsys):
    """``main()`` debe escribir el mensaje de la aplicación en stdout."""
    app.main()

    salida = capsys.readouterr().out

    assert MENSAJE_ESPERADO in salida, f"Salida inesperada: {salida!r}"
    # La salida debe terminar en salto de línea para que la consola quede limpia.
    assert salida.endswith("\n"), "La salida debe terminar en un salto de línea"


def test_main_no_escribe_en_stderr(capsys):
    """Una ejecución correcta no debe generar mensajes de error."""
    app.main()

    assert capsys.readouterr().err == ""


def test_main_es_idempotente(capsys):
    """Ejecutar ``main()`` dos veces debe producir exactamente la misma salida."""
    app.main()
    primera = capsys.readouterr().out

    app.main()
    segunda = capsys.readouterr().out

    assert primera == segunda


def test_app_es_ejecutable_como_script():
    """Ejecutar ``python app.py`` debe terminar con código 0 y mostrar el mensaje."""
    resultado = subprocess.run(
        [sys.executable, "app.py"],
        cwd=RAIZ,
        capture_output=True,
        text=True,
        check=False,
    )

    assert resultado.returncode == 0, resultado.stderr
    assert MENSAJE_ESPERADO in resultado.stdout
