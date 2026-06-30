#!/usr/bin/env python3
"""Extract text from 10 priority PDFs using PyMuPDF (fitz)."""

import fitz
import os
import sys

# Source and destination
SRC = "/Users/fabiotakwara/Documents/GitHub/Takwara-Tech/Chatbot_Takwara/fontes-privadas/"
DST = "/Users/fabiotakwara/Documents/GitHub/Mentoria_Tecnologia_Takwara/TRIAGEM_BRUTA/PDF_EXTRAIDOS/"

# Mapping of source PDF filenames -> output .md filenames
PDFS = {
    "2019.Tese_BAmbus Nativos do Brasil_Cadeia Produtiva e Conservação-UNICAMPpdf.pdf": "TESE-BAMBUS-NATIVOS-UNICAMP.md",
    "2021 -UNICAMP-Geodesicas.pdf": "TESE-GEODESICAS-UNICAMP.md",
    "Tese-FIXACAO DE CARBONO-SAOCARLOS.pdf": "TESE-CARBONO-SAOCARLOS.md",
    "2018_VitorHugoSilvaMarcal.pdf": "DISSERT-VITOR-MARCAL.md",
    "2018 - Bambu Laminado - Jose_Ricardo.pdf": "DISSERT-BAMBU-LAMINADO.md",
    "Dissert_Vianna_DeniseL PU Mamona proteses.pdf": "DISSERT-PU-MAMONA-PROTESES.md",
    "Silva_Rodolfo Gomes Tratamento pirolenhoso (Unicampi 2011).pdf": "DISSERT-TRATAMENTO-PIROLENHOSO.md",
    "Bambus_no_Brasil - EMBRAPA dez17.pdf": "EMBRAPA-BAMBUS-BRASIL.md",
    "0001 ENSAIOS IMPERVEG- CIV-Anna Carolina Aiex Naccache.pdf": "ENSAIOS-IMPERVEG-NACCACHE.md",
    "Filho - 2018 - BAMBU LAMINADO COLADO PRODUCAO, CARACTERIZACAO E .pdf": "BLC-FILHO-2018.md",
}

os.makedirs(DST, exist_ok=True)

results = []

for src_name, dst_name in sorted(PDFS.items()):
    src_path = os.path.join(SRC, src_name)
    dst_path = os.path.join(DST, dst_name)
    
    if not os.path.exists(src_path):
        results.append((src_name, "NOT FOUND", 0, "File does not exist"))
        continue
    
    try:
        doc = fitz.open(src_path)
        num_pages = len(doc)
        text_parts = []
        for page in doc:
            t = page.get_text()
            text_parts.append(t)
        full_text = "\n".join(text_parts)
        doc.close()
        
        # Write to .md
        with open(dst_path, "w", encoding="utf-8") as f:
            f.write(f"# {dst_name.replace('.md','')}\n\n")
            f.write(f"**Fonte:** {src_name}\n")
            f.write(f"**Páginas:** {num_pages}\n")
            f.write(f"**Extraído em:** {__import__('datetime').datetime.now().isoformat()}\n\n")
            f.write("---\n\n")
            f.write(full_text)
        
        char_count = len(full_text)
        status = "OK" if char_count > 100 else "LOW TEXT"
        results.append((src_name, dst_name, num_pages, f"{status} ({char_count} chars)"))
    except Exception as e:
        results.append((src_name, dst_name, 0, f"ERROR: {str(e)}"))

# Print summary
print("=" * 80)
print("EXTRACTION SUMMARY")
print("=" * 80)
print(f"{'Source PDF':<70} {'Pages':>6} {'Status'}")
print("-" * 80)
for src_name, dst_name, pages, status in results:
    short_src = src_name[:65] + "..." if len(src_name) > 65 else src_name
    print(f"{short_src:<70} {pages:>6}  {status}")
print("=" * 80)
