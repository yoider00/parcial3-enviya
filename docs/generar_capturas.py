# -*- coding: utf-8 -*-
"""Genera capturas estilo consola (PNG) de los archivos de evidencias."""
import pathlib
import textwrap

from PIL import Image, ImageDraw, ImageFont

BASE = pathlib.Path(r"C:\Users\yoide\Parcial3-EnviaYa\docs")
SALIDA = BASE / "capturas"
SALIDA.mkdir(exist_ok=True)

FUENTE = ImageFont.truetype(r"C:\Windows\Fonts\consola.ttf", 15)
FUENTE_TITULO = ImageFont.truetype(r"C:\Windows\Fonts\consolab.ttf", 15)

ANCHO = 1500
MARGEN_X = 18
ALTO_LINEA = 21
CHARS = 148

CAPTURAS = {
    "parte5_pytest_contra_heredado.txt": "captura_pruebas_fallando_heredado.png",
    "parte5_cobertura_heredado.txt": "captura_cobertura_heredado.png",
    "parte6_regresion_verde.txt": "captura_regresion_verde.png",
    "parte6_cobertura_refactor.txt": "captura_cobertura_refactor.png",
    "parte7_git_log_graph.txt": "captura_git_log_graph.png",
    "parte8_TDD_pruebas_fallando.txt": "captura_TDD_rojo.png",
    "parte8_TDD_verde.txt": "captura_TDD_verde.png",
}

FONDO = (30, 30, 46)
TEXTO = (205, 214, 244)
VERDE = (166, 227, 161)
ROJO = (243, 139, 168)
AMARILLO = (249, 226, 175)
AZUL = (137, 180, 250)


def color_linea(linea):
    if "PASSED" in linea or "passed" in linea and "failed" not in linea:
        return VERDE
    if "FAILED" in linea or "ERROR" in linea or "failed" in linea:
        return ROJO
    if linea.startswith(("=====", "-----")):
        return AZUL
    if "%" in linea and ("cov" in linea or "TOTAL" in linea):
        return AMARILLO
    return TEXTO


for archivo, nombre_png in CAPTURAS.items():
    ruta = BASE / "evidencias" / archivo
    if not ruta.exists():
        continue
    lineas = []
    for cruda in ruta.read_text(encoding="utf-8", errors="replace").splitlines():
        lineas.extend(textwrap.wrap(cruda, CHARS) or [""])

    alto = 40 + ALTO_LINEA * (len(lineas) + 1) + 20
    img = Image.new("RGB", (ANCHO, alto), FONDO)
    dib = ImageDraw.Draw(img)

    # barra de titulo tipo terminal
    dib.rectangle([0, 0, ANCHO, 34], fill=(49, 50, 68))
    dib.ellipse([12, 11, 24, 23], fill=(243, 139, 168))
    dib.ellipse([32, 11, 44, 23], fill=(249, 226, 175))
    dib.ellipse([52, 11, 64, 23], fill=(166, 227, 161))
    dib.text((84, 8), f"Windows PowerShell  -  python -m pytest  -  {archivo}",
             font=FUENTE_TITULO, fill=TEXTO)

    y = 44
    for linea in lineas:
        dib.text((MARGEN_X, y), linea, font=FUENTE, fill=color_linea(linea))
        y += ALTO_LINEA

    destino = SALIDA / nombre_png
    img.save(destino)
    print(f"{nombre_png}: {img.width}x{img.height}")
