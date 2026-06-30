#!/usr/bin/env python3
"""Extract text from Shara Carvalho Lopes dissertation PDF using pypdf."""
import sys

pdf_path = "/Users/fabiotakwara/Documents/Imperveg/Shara Carvalho Lopes - Dissertação.pdf"

try:
    from pypdf import PdfReader
    reader = PdfReader(pdf_path)
    text = ""
    for i, page in enumerate(reader.pages):
        txt = page.extract_text()
        text += f"\n===PAGE {i+1}===\n{txt}"
    out_path = "/Users/fabiotakwara/Documents/GitHub/Mentoria_Tecnologia_Takwara/_shara_extracted.txt"
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(text)
    print(f"SUCCESS: {len(text)} chars extracted to {out_path}")
    print(f"Total pages: {len(reader.pages)}")
except Exception as e:
    print(f"ERROR: {e}")
