#!/bin/bash
# OCR Processor for scanned PDFs
# Uses: PyMuPDF (fitz) for rendering, Tesseract for OCR

PDF_DIR="/Users/fabiotakwara/Documents/IFB Relatorio Final/Bibliografia Consultada"
OUT_DIR="/Users/fabiotakwara/Documents/GitHub/Mentoria_Tecnologia_Takwara/TRIAGEM_BRUTA/PDF_EXTRAIDOS"
TEMP_DIR="/Users/fabiotakwara/Desktop/ocr_temp"
PYTHON="/Users/fabiotakwara/miniconda3/envs/whisper_env/bin/python3"
TESSERACT="/Users/fabiotakwara/miniconda3/envs/whisper_env/bin/tesseract"

mkdir -p "$TEMP_DIR" "$OUT_DIR"

# Define PDFs as array of (path, output_name)
PDFS=(
  "$PDF_DIR/Bambu recurso do sec 21.pdf:BAMBU-RECURSO-SEC21"
  "$PDF_DIR/Rede inter Bambu Ratan.pdf:REDE-INTER-BAMBU-RATAN"
  "$PDF_DIR/FISPQ - ENSAIOS Diversos/CATALOGO-CORES-KEHLCOAT1.pdf:CATALOGO-CORES-KEHLCOAT1"
  "$PDF_DIR/FISPQ - ENSAIOS Diversos/FISPQ - Aglomerante Kehl.pdf:FISPQ-AGLOMERANTE-KEHL"
  "$PDF_DIR/FISPQ - ENSAIOS Diversos/LAudo potabilidade.pdf:LAUDO-POTABILIDADE"
  "$PDF_DIR/FISPQ - ENSAIOS Diversos/LAudo potabilidade2.pdf:LAUDO-POTABILIDADE2"
  "$PDF_DIR/FISPQ - ENSAIOS Diversos/UNICAMP - Teste de Biodegradação 2000.pdf:UNICAMP-TESTE-BIODEGRADACAO-2000"
  "$PDF_DIR/FISPQ - ENSAIOS Diversos/UNICAMP - Toxicidade Aguda via Oral 2003 - Signed.pdf:UNICAMP-TOXICIDADE-AGUDA-ORAL-2003"
  "$PDF_DIR/Teses-artigos tecnicos/Biodiesel.pdf:BIODIESEL"
  "$PDF_DIR/Teses-artigos tecnicos/USP - Avaliacao Experimental de Compostagem 2006.pdf:USP-AVALIACAO-EXPERIMENTAL-COMPOSTAGEM-2006"
)

for entry in "${PDFS[@]}"; do
  INPUT="${entry%%:*}"
  BASENAME="${entry##*:}"
  
  echo ""
  echo "========================================"
  echo "PROCESSING: $BASENAME"
  echo "Source: $INPUT"
  echo "========================================"
  
  # Clean temp directory before each PDF
  rm -f "$TEMP_DIR"/*.png "$TEMP_DIR"/*.txt
  
  # Step 1: Render PDF pages to images on Desktop
  echo "  Rendering pages..."
  "$PYTHON" -c "
import fitz, sys, os
pdf_path = sys.argv[1]
temp_dir = sys.argv[2]
doc = fitz.open(pdf_path)
print(f'  PDF has {len(doc)} pages')
for i in range(len(doc)):
    page = doc[i]
    pix = page.get_pixmap(dpi=200)
    out_path = os.path.join(temp_dir, f'page_{i}.png')
    pix.save(out_path)
    if i % 10 == 0:
        print(f'  Rendered page {i}')
doc.close()
print(f'  Done rendering {len(doc)} pages')
" "$INPUT" "$TEMP_DIR"
  
  # Step 2: OCR each rendered page
  echo "  OCRing pages..."
  cd "$TEMP_DIR"
  PAGE_COUNT=$(ls -1 page_*.png 2>/dev/null | wc -l)
  echo "  Found $PAGE_COUNT images to OCR"
  
  for page_file in page_*.png; do
    base="${page_file%.png}"
    "$TESSERACT" "$page_file" "$base" -l por+eng --psm 3 2>/dev/null
  done
  
  # Step 3: Combine all .txt into a single .md file
  echo "  Combining results..."
  OUTPUT_FILE="$OUT_DIR/${BASENAME}_OCR.md"
  
  echo "# OCR Extraído: ${BASENAME}" > "$OUTPUT_FILE"
  echo "" >> "$OUTPUT_FILE"
  echo "**Fonte:** $INPUT" >> "$OUTPUT_FILE"
  echo "**Data do OCR:** $(date '+%Y-%m-%d %H:%M:%S')" >> "$OUTPUT_FILE"
  echo "**Idiomas:** por+eng" >> "$OUTPUT_FILE"
  echo "" >> "$OUTPUT_FILE"
  echo "---" >> "$OUTPUT_FILE"
  echo "" >> "$OUTPUT_FILE"
  
  TXT_COUNT=0
  for txt_file in $(ls page_*.txt 2>/dev/null | sort -t_ -k2 -n); do
    TXT_COUNT=$((TXT_COUNT + 1))
    echo "## Página $TXT_COUNT" >> "$OUTPUT_FILE"
    echo "" >> "$OUTPUT_FILE"
    cat "$txt_file" >> "$OUTPUT_FILE"
    echo "" >> "$OUTPUT_FILE"
    echo "---" >> "$OUTPUT_FILE"
    echo "" >> "$OUTPUT_FILE"
  done
  
  echo "  Combined $TXT_COUNT pages into $OUTPUT_FILE"
  
  # Step 4: Clean up temp files
  echo "  Cleaning up temp files..."
  rm -f "$TEMP_DIR"/*.png "$TEMP_DIR"/*.txt
  
  # Show result size
  FILE_SIZE=$(wc -c < "$OUTPUT_FILE")
  echo "  Output file size: $FILE_SIZE bytes"
done

echo ""
echo "========================================"
echo "ALL 10 PDFs PROCESSED"
echo "========================================"
echo ""
echo "Output directory: $OUT_DIR"
ls -la "$OUT_DIR"/*_OCR.md 2>/dev/null
