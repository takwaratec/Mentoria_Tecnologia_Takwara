#!/usr/bin/env python3
"""Extract text from 10 priority PDFs using PyMuPDF (fitz) - v2 with exact paths."""

import fitz
import os
import sys
from datetime import datetime

SRC = "/Users/fabiotakwara/Documents/GitHub/Takwara-Tech/Chatbot_Takwara/fontes-privadas/"
DST = "/Users/fabiotakwara/Documents/GitHub/Mentoria_Tecnologia_Takwara/TRIAGEM_BRUTA/PDF_EXTRAIDOS/"

# Exact source paths -> output .md filenames
PDFS = [
    # Priority 1: from root 
    (SRC + "2019.Tese_BAmbus Nativos do Brasil_Cadeia Produtiva e Conservação-UNICAMPpdf.pdf",
     "TESE-BAMBUS-NATIVOS-UNICAMP.md"),
    # Note: the file on disk uses "Conservação" with combining chars, try both
    (SRC + "2019.Tese_BAmbus Nativos do Brasil_Cadeia Produtiva e Conservação-UNICAMPpdf.pdf",
     "TESE-BAMBUS-NATIVOS-UNICAMP.md"),
    
    (SRC + "2021 -UNICAMP-Geodesicas.pdf",
     "TESE-GEODESICAS-UNICAMP.md"),
    
    (SRC + "Tese-FIXAÇAO DE CARBONO-SAOCARLOS.pdf",
     "TESE-CARBONO-SAOCARLOS.md"),
    (SRC + "Tese-FIXACAO DE CARBONO-SAOCARLOS.pdf",
     "TESE-CARBONO-SAOCARLOS.md"),
    
    (SRC + "2018_VitorHugoSilvaMarçal.pdf",
     "DISSERT-VITOR-MARCAL.md"),
    (SRC + "2018_VitorHugoSilvaMarcal.pdf",
     "DISSERT-VITOR-MARCAL.md"),
    
    (SRC + "2018 - Bambu Laminado - Jose_Ricardo.pdf",
     "DISSERT-BAMBU-LAMINADO.md"),
    
    # PU Vegetal subdir
    (SRC + "PU Vegetal/Dissert_Vianna_DeniseL PU Mamona proteses.pdf",
     "DISSERT-PU-MAMONA-PROTESES.md"),
    
    # Pirolenhoso subdir
    (SRC + "Pirolenhoso/Silva_Rodolfo Gomes Tratamento pirolenhoso (Unicampi 2011).pdf",
     "DISSERT-TRATAMENTO-PIROLENHOSO.md"),
    
    (SRC + "Bambus_no_Brasil - EMBRAPA dez17.pdf",
     "EMBRAPA-BAMBUS-BRASIL.md"),
    
    # PU Vegetal subdir
    (SRC + "PU Vegetal/0001 ENSAIOS IMPERVEG- CIV-Anna Carolina Aiex Naccache.pdf",
     "ENSAIOS-IMPERVEG-NACCACHE.md"),
    
    # Propiedade Fisicas subdir
    (SRC + "Propiedade Fisicas/Filho - 2018 - BAMBU LAMINADO COLADO PRODUÇÃO, CARACTERIZAÇÃO E .pdf",
     "BLC-FILHO-2018.md"),
]

os.makedirs(DST, exist_ok=True)

# Deduplicate by output filename (keep first successful)
done = {}
results = []

for src_path, dst_name in PDFS:
    if dst_name in done:
        continue  # already have a match
    
    src_path = os.path.normpath(src_path)
    if not os.path.exists(src_path):
        continue  # try next fallback
    
    dst_path = os.path.join(DST, dst_name)
    
    try:
        doc = fitz.open(src_path)
        num_pages = len(doc)
        text_parts = []
        for page in doc:
            t = page.get_text()
            text_parts.append(t)
        full_text = "\n".join(text_parts)
        doc.close()
        
        with open(dst_path, "w", encoding="utf-8") as f:
            f.write(f"# {dst_name.replace('.md','')}\n\n")
            f.write(f"**Fonte:** {os.path.basename(src_path)}\n")
            f.write(f"**Páginas:** {num_pages}\n")
            f.write(f"**Extraído em:** {datetime.now().isoformat()}\n\n")
            f.write("---\n\n")
            f.write(full_text)
        
        char_count = len(full_text)
        status = "OK" if char_count > 100 else "LOW TEXT"
        done[dst_name] = (os.path.basename(src_path), num_pages, f"{status} ({char_count} chars)")
    except Exception as e:
        done[dst_name] = (os.path.basename(src_path), 0, f"ERROR: {str(e)}")

# Print summary
print("=" * 80)
print("EXTRACTION SUMMARY")
print("=" * 80)
print(f"{'Output File':<50} {'Pages':>6}  {'Status'}")
print("-" * 80)
for dst_name in sorted(done.keys()):
    basename, pages, status = done[dst_name]
    print(f"{dst_name:<50} {pages:>6}  {status}")
print("=" * 80)

# List any failures
print("\nFiles extracted to:", DST)
for f in sorted(os.listdir(DST)):
    if f.endswith('.md'):
        sz = os.path.getsize(os.path.join(DST, f))
        print(f"  {f}: {sz:,} bytes")
