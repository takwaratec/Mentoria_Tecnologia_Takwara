#!/usr/bin/env python3
"""Extract text from Takwara-Tech PDFs, save as .md in PARA_REVISAO_TT."""
import fitz, os, sys, glob, textwrap

TT = "/Users/fabiotakwara/Documents/GitHub/Takwara-Tech"
OUT = "/Users/fabiotakwara/Documents/GitHub/Mentoria_Tecnologia_Takwara/TRIAGEM_BRUTA/PARA_REVISAO_TT"

# Priority 1: Chatbot_Takwara technical references
src_dirs = [
    "Chatbot_Takwara/fontes-privadas",
    "Chatbot_Takwara/fontes-privadas/Pirolenhoso",
    "Chatbot_Takwara/fontes-privadas/Manejo Exoticas",
    "Chatbot_Takwara/fontes-privadas/Tratamento Bambu",
    "Chatbot_Takwara/fontes-privadas/Propiedade Fisicas",
    "Chatbot_Takwara/fontes-privadas/PU Vegetal",
    "Chatbot_Takwara/fontes-privadas/Fabio Takwara",
    "Chatbot_Takwara/fontes-privadas/Geodesicas",
    "Chatbot_Takwara/fontes-privadas/Normas",
    "Chatbot_Takwara/fontes-privadas/Treliças",
    "A8. Anais da pesquisa",
    "Chapada Diamantina",
    "BAncadas",
]

total = 0
errors = []
for sd in src_dirs:
    full = os.path.join(TT, "docs", sd) if os.path.exists(os.path.join(TT, "docs", sd)) else os.path.join(TT, sd)
    if not os.path.exists(full):
        # Try without docs/
        full = os.path.join(TT, sd)
    if not os.path.exists(full):
        print(f"⚠️  Pasta não encontrada: {sd}")
        continue
    
    pdfs = sorted(glob.glob(os.path.join(full, "*.pdf")))
    print(f"\n📂 {sd} ({len(pdfs)} PDFs)")
    
    for pdf_path in pdfs:
        fname = os.path.basename(pdf_path)
        md_name = fname.replace(".pdf", ".md").replace(" ", "_").replace("__", "_")
        # Sanitize filename
        md_name = "".join(c if c.isalnum() or c in "._- " else "_" for c in md_name)
        out_path = os.path.join(OUT, md_name)
        
        if os.path.exists(out_path):
            print(f"  ⏭️  Já existe: {md_name}")
            continue
        
        try:
            doc = fitz.open(pdf_path)
            pages = len(doc)
            texts = []
            for i in range(pages):
                t = doc[i].get_text().strip()
                if t:
                    texts.append(f"--- Página {i+1} ---\n{t}")
            doc.close()
            
            if not texts:
                print(f"  ⚠️  Sem texto: {fname}")
                continue
            
            full_text = "\n\n".join(texts)
            with open(out_path, "w", encoding="utf-8") as f:
                f.write(f"# {fname.replace('.pdf','')}\n\n")
                f.write(f"> Extraído de: {pdf_path}\n")
                f.write(f"> Páginas: {pages}\n")
                f.write(f"> Data de extração: 28/06/2026\n\n")
                f.write(f"---\n\n")
                f.write(full_text)
            
            size_kb = os.path.getsize(out_path) / 1024
            print(f"  ✅ {md_name} ({pages}pgs, {size_kb:.0f}KB)")
            total += 1
            
        except Exception as e:
            errors.append(f"{fname}: {e}")
            print(f"  ❌ {fname}: {e}")

print(f"\n\n{'='*50}")
print(f"Total extraídos: {total}")
if errors:
    print(f"Erros: {len(errors)}")
    for e in errors[:5]:
        print(f"  - {e}")
