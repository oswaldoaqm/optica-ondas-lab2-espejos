"""Genera los PDF del documento y de la presentación a partir de sus HTML.

Uso:
    python generar_pdfs.py                              # sin enlace del video
    python generar_pdfs.py --video https://youtu.be/... # con el enlace en la portada

Requiere: pip install playwright && python -m playwright install chromium
"""
import argparse
import html
from pathlib import Path

from playwright.sync_api import sync_playwright

RAIZ = Path(__file__).resolve().parent
PIE = (
    '<div style="width:100%; font-family:DejaVu Sans, sans-serif; font-size:7.5pt; color:#5d6b7a;'
    ' margin:0 20mm; padding-top:4pt; border-top:0.6pt solid #d5dbe2; display:flex;'
    ' justify-content:space-between;">'
    "<span>Laboratorio 2 — Formación de imágenes en espejos cóncavos y convexos · Grupo 5 · UTEC 2026-II</span>"
    '<span class="pageNumber"></span></div>'
)
MARCADOR_VIDEO = '<span class="falta">[FALTA: enlace de YouTube]</span>'


def documento(navegador, video):
    fuente = RAIZ / "documento" / "documento.html"
    texto = fuente.read_text(encoding="utf-8")
    if video:
        enlace = html.escape(video)
        texto = texto.replace(MARCADOR_VIDEO, f'<a href="{enlace}">{enlace}</a>')
    temporal = fuente.with_name("_documento_render.html")
    temporal.write_text(texto, encoding="utf-8")
    try:
        pagina = navegador.new_page()
        pagina.goto(temporal.as_uri(), wait_until="networkidle")
        pagina.pdf(
            path=str(RAIZ / "documento" / "Lab2-Espejos-Grupo5-Documento.pdf"),
            format="A4",
            print_background=True,
            display_header_footer=True,
            header_template="<div></div>",
            footer_template=PIE,
            prefer_css_page_size=True,
        )
        pagina.close()
    finally:
        temporal.unlink(missing_ok=True)


def presentacion(navegador):
    fuente = RAIZ / "presentacion" / "presentacion.html"
    pagina = navegador.new_page(viewport={"width": 1920, "height": 1080})
    pagina.goto(fuente.as_uri(), wait_until="networkidle")
    pagina.evaluate("document.fonts.ready")
    pagina.pdf(
        path=str(RAIZ / "presentacion" / "Lab2-Espejos-Grupo5-Presentacion.pdf"),
        width="1920px",
        height="1080px",
        print_background=True,
        prefer_css_page_size=True,
    )
    pagina.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--video", help="enlace de YouTube para la portada del documento")
    args = parser.parse_args()
    with sync_playwright() as p:
        try:
            navegador = p.chromium.launch()
        except Exception:
            navegador = p.chromium.launch(channel="chrome")  # usa el Chrome instalado
        documento(navegador, args.video)
        presentacion(navegador)
        navegador.close()
    print("PDF generados en documento/ y presentacion/")
