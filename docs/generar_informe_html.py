# -*- coding: utf-8 -*-
"""Genera Informe_Parcial3.html desde el markdown, con anexos de evidencias.
Los diagramas Mermaid se insertan como imagenes PNG pre-renderizadas."""
import html as _html
import pathlib
import re as _re

import markdown

base = pathlib.Path(r"C:\Users\yoide\Parcial3-EnviaYa\docs")
texto = (base / "Informe_Parcial3.md").read_text(encoding="utf-8")

evidencias = {
    "Anexo A - pytest contra el heredado (11 fallas reveladas)": "parte5_pytest_contra_heredado.txt",
    "Anexo B - cobertura del heredado (pytest-cov)": "parte5_cobertura_heredado.txt",
    "Anexo C - regresion en verde v2.0.0 (27/27)": "parte6_regresion_verde.txt",
    "Anexo D - cobertura de la version refactorizada": "parte6_cobertura_refactor.txt",
    "Anexo E - git log --oneline --graph --all": "parte7_git_log_graph.txt",
    "Anexo F - TDD rojo: CHG-001 pruebas fallando": "parte8_TDD_pruebas_fallando.txt",
    "Anexo G - TDD verde: 30/30 pasan": "parte8_TDD_verde.txt",
}

anexos = ["", "---", "", "# Anexos (evidencias de ejecucion)", ""]
for titulo, archivo in evidencias.items():
    ruta = base / "evidencias" / archivo
    if ruta.exists():
        lineas = ruta.read_text(encoding="utf-8", errors="replace").splitlines()
        while lineas and lineas[-1].strip() == "":
            lineas.pop()
        anexos += [f"## {titulo}", "", "```text", *lineas, "```", ""]
texto += "\n".join(anexos)

html_body = markdown.markdown(
    texto,
    extensions=["tables", "fenced_code", "sane_lists", "smarty"],
    output_format="html5",
)

# Reemplazar los bloques <pre><code class="language-mermaid"> por imagenes
# pre-renderizadas (docs/capturas/*.png).

flujo_img = (
    '<div class="fila-diagrama">'
    '<figure><img src="capturas/diagrama_flujo_a.png" alt="Grafo de flujo, parte 1">'
    "<figcaption>Parte 1 · entrada, tramos y zona</figcaption></figure>"
    '<figure><img src="capturas/diagrama_flujo_b.png" alt="Grafo de flujo, parte 2">'
    "<figcaption>Parte 2 · finde y descuentos<br>(N6/N7/N8 entran a Q7)</figcaption></figure>"
    '<figure><img src="capturas/diagrama_flujo_c.png" alt="Grafo de flujo, parte 3">'
    "<figcaption>Parte 3 · cupón, mínimo y salida<br>(Q10 continúa aquí)</figcaption></figure>"
    "</div>"
)

clases_img = (
    '<div class="diagrama-centro">'
    '<figure><img src="capturas/diagrama_clases.png" alt="Diagrama de clases UML del patrón Estrategia">'
    "<figcaption>Patrón Estrategia aplicado al recargo por zona</figcaption></figure>"
    "</div>"
)

bloques = _re.findall(r'<pre><code class="language-mermaid">.*?</code></pre>', html_body, flags=_re.S)
assert len(bloques) == 2, f"se esperaban 2 bloques mermaid, hay {len(bloques)}"
html_body = html_body.replace(bloques[0], flujo_img, 1)
html_body = html_body.replace(bloques[1], clases_img, 1)

css = """
<style>
  @page { size: A4; margin: 18mm 16mm; }
  body { font-family: Arial, Helvetica, sans-serif; font-size: 11pt; line-height: 1.45;
         color: #000000; background: #ffffff; }
  h1 { font-size: 20pt; color: #000; border-bottom: 3px solid #000; padding-bottom: 6px; }
  h2 { font-size: 15pt; color: #000; border-bottom: 1px solid #555; padding-bottom: 4px; margin-top: 26px; }
  h3 { font-size: 12.5pt; color: #000; margin-top: 18px; }
  table { border-collapse: collapse; width: 100%; margin: 10px 0; font-size: 9.5pt; }
  th { background: #000; color: #fff; padding: 6px 8px; text-align: left; }
  td { border: 1px solid #555; padding: 5px 8px; color: #000; }
  tr:nth-child(even) td { background: #f0f0f0; }
  code { font-family: 'Courier New', monospace; background: #ececec; padding: 1px 4px;
         border-radius: 3px; font-size: 9.5pt; color: #000; }
  pre { background: #f7f7f7; border: 1px solid #bbb; border-radius: 6px; padding: 10px 12px; overflow-x: hidden; }
  pre code { background: none; font-size: 9pt; line-height: 1.35; white-space: pre-wrap; word-break: break-word; }
  blockquote { border-left: 4px solid #000; background: #f2f2f2; padding: 8px 14px; margin: 10px 0; }
  figure { margin: 4px; text-align: center; }
  figure img { max-width: 100%; height: auto; }
  figcaption { font-size: 8.5pt; color: #000; margin-top: 4px; }
  .fila-diagrama { display: flex; gap: 6px; align-items: flex-start; justify-content: center; }
  .fila-diagrama figure:nth-child(1) { width: 56%; }
  .fila-diagrama figure:nth-child(2) { width: 21%; }
  .fila-diagrama figure:nth-child(3) { width: 21%; }
  .diagrama-centro { text-align: center; }
  .diagrama-centro figure { display: inline-block; width: 65%; }
</style>
"""

html = (
    '<!DOCTYPE html><html lang="es"><head><meta charset="utf-8">'
    "<title>Parcial 3 - Informe - Yoider Brito</title>"
    + css + "</head><body>" + html_body + "</body></html>"
)

salida = base / "Informe_Parcial3.html"
salida.write_text(html, encoding="utf-8")
print("HTML generado:", salida)
