# -*- coding: utf-8 -*-
"""Genera Informe_Parcial3.html desde el markdown, con anexos de evidencias."""
import markdown
import pathlib

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

# Convertir bloques <pre><code class="language-mermaid"> en <div class="mermaid">
# para que mermaid.run() los procese y los dibuje.
import html as _html
import re as _re

html_body = _re.sub(
    r'<pre><code class="language-mermaid">(.*?)</code></pre>',
    lambda m: '<div class="mermaid">' + _html.unescape(m.group(1)) + "</div>",
    html_body,
    flags=_re.S,
)

css = """
<style>
  @page { size: A4; margin: 18mm 16mm; }
  body { font-family: 'Segoe UI', Calibri, sans-serif; font-size: 11pt; line-height: 1.45; color: #1a1a2e; }
  h1 { font-size: 20pt; color: #0d3b66; border-bottom: 3px solid #0d3b66; padding-bottom: 6px; }
  h2 { font-size: 15pt; color: #0d3b66; border-bottom: 1px solid #9db4c0; padding-bottom: 4px; margin-top: 26px; }
  h3 { font-size: 12.5pt; color: #14532d; margin-top: 18px; }
  table { border-collapse: collapse; width: 100%; margin: 10px 0; font-size: 9.5pt; }
  th { background: #0d3b66; color: white; padding: 6px 8px; text-align: left; }
  td { border: 1px solid #b8c4cc; padding: 5px 8px; }
  tr:nth-child(even) td { background: #f2f7fa; }
  code { font-family: Consolas, monospace; background: #eef2f5; padding: 1px 4px; border-radius: 3px; font-size: 9.5pt; }
  pre { background: #f6f8fa; border: 1px solid #d0d7de; border-radius: 6px; padding: 10px 12px; overflow-x: hidden; }
  pre code { background: none; font-size: 9pt; line-height: 1.35; white-space: pre-wrap; word-break: break-word; }
  blockquote { border-left: 4px solid #f4a261; background: #fff8ef; padding: 8px 14px; margin: 10px 0; }
</style>
"""

mermaid_js = ""

ruta_mermaid = base / "mermaid.min.js"
if not ruta_mermaid.exists():
    import urllib.request
    urllib.request.urlretrieve(
        "https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js",
        str(ruta_mermaid),
    )
    print("mermaid.min.js descargado")
codigo_mermaid = ruta_mermaid.read_text(encoding="utf-8")
mermaid_js = (
    "<script>" + codigo_mermaid + "</script>"
    "<script>window.addEventListener('load', function () {"
    "mermaid.initialize({ startOnLoad: false, theme: 'default' });"
    "mermaid.run().then(function () { document.title = 'MERMAID_READY'; });"
    "});</script>"
)

html = (
    '<!DOCTYPE html><html lang="es"><head><meta charset="utf-8">'
    "<title>Parcial 3 - Informe - Yoider Brito</title>"
    + css + mermaid_js + "</head><body>" + html_body + "</body></html>"
)

salida = base / "Informe_Parcial3.html"
salida.write_text(html, encoding="utf-8")
print("HTML generado:", salida)
