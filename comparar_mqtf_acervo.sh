#!/bin/bash
# Script to compare MQTF technical reviews with Acervo documents
# Usage: bash comparar_mqtf_acervo.sh

set -e

MQTF_BASE="/Users/fabiotakwara/Documents/GitHub/UnB/Mulheres-Tecem-Amazonia/_RESEARCH_RAW/BACKUP_LOCAL/04_PESQUISA_ANDAMENTO/ACERVO_DIGITAL_WTF/02_TECHNICAL_REVIEWS"
ACERVO_BASE="/Users/fabiotakwara/Documents/GitHub/Analises e escrita científica/docs"

echo "============================================================"
echo "  COMPARACAO: MQTF Technical Reviews vs Acervo Cientifico"
echo "============================================================"
echo ""

# --- Step 1: Collect all .md basenames from Acervo ---
echo "[1/4] Coletando basenames do Acervo..."
ACERVO_NAMES=""
ACERVO_NAMES_NOEXT=""
while IFS= read -r -d '' f; do
  bn=$(basename "$f")
  ACERVO_NAMES="$ACERVO_NAMES"$'\n'"$bn"
  # Without extension
  base_noext="${bn%.md}"
  ACERVO_NAMES_NOEXT="$ACERVO_NAMES_NOEXT"$'\n'"$base_noext"
done < <(find "$ACERVO_BASE" -name "*.md" -type f -print0)
ACERVO_COUNT=$(echo "$ACERVO_NAMES" | grep -c .)
echo "  Total .md no Acervo: $ACERVO_COUNT"
echo ""

# Put in sorted arrays for fast lookup
mapfile -t acervo_arr < <(echo "$ACERVO_NAMES" | grep . | sort)
mapfile -t acervo_noext_arr < <(echo "$ACERVO_NAMES_NOEXT" | grep . | sort)

# Build associative sets
declare -A ACERVO_SET
declare -A ACERVO_SET_NOEXT
for n in "${acervo_arr[@]}"; do
  ACERVO_SET["$n"]=1
done
for n in "${acervo_noext_arr[@]}"; do
  ACERVO_SET_NOEXT["$n"]=1
done

echo "[2/4] Coletando basenames do MQTF..."
echo ""

# --- Step 2: Process each thematic folder ---
THEMATIC_FOLDERS=(
  "01_CIENTIFICO"
  "Bambu"
  "Bioeconomia"
  "Biomateriais"
  "Construcao_Sustentavel"
  "Inovacao"
  "Outros"
  "PU_Vegetal"
  "Saneamento"
  "Saneamento_Ecológico"
  "Saúde_Ambiental"
  "Tecnoveg-Imperveg"
)

OVERALL_MQTF=0
OVERALL_IN_ACERVO=0
OVERALL_MISSING=0
OVERALL_DUPLICATES=0

for folder in "${THEMATIC_FOLDERS[@]}"; do
  folder_path="$MQTF_BASE/$folder"
  if [ ! -d "$folder_path" ]; then
    echo "  *** AVISO: Pasta '$folder' nao encontrada em MQTF ***"
    echo ""
    continue
  fi

  # Collect all .md files in this thematic folder (recursively)
  mqtf_files=()
  sub_label=""
  
  # For 01_CIENTIFICO, use subfolders as sub-thematic groups
  if [ "$folder" = "01_CIENTIFICO" ]; then
    echo "--- $folder/ ---"
    # Process each subfolder
    for sub in "$folder_path"/*/; do
      subname=$(basename "$sub")
      sub_files=()
      while IFS= read -r -d '' f; do
        sub_files+=("$f")
      done < <(find "$sub" -name "*.md" -type f -print0 2>/dev/null)
      
      sub_count=${#sub_files[@]}
      if [ "$sub_count" -eq 0 ]; then
        continue
      fi
      
      sub_in_acervo=0
      sub_missing=()
      sub_acervo_names_list=()
      
      for f in "${sub_files[@]}"; do
        bn=$(basename "$f")
        base_noext="${bn%.md}"
        OVERALL_MQTF=$((OVERALL_MQTF + 1))
        
        # Check exact match first
        if [[ -n "${ACERVO_SET[$bn]:-}" ]]; then
          sub_in_acervo=$((sub_in_acervo + 1))
          sub_acervo_names_list+=("$bn")
        elif [[ -n "${ACERVO_SET_NOEXT[$base_noext]:-}" ]]; then
          sub_in_acervo=$((sub_in_acervo + 1))
          sub_acervo_names_list+=("$bn")
        else
          sub_missing+=("$bn")
        fi
      done
      
      overall_in_acervo=$((OVERALL_IN_ACERVO + sub_in_acervo))
      
      echo "  ${subname}:"
      echo "    MQTF:     ${sub_count} arquivos"
      echo "    Acervo:   ${sub_in_acervo} encontrados"
      echo "    Faltam:   ${#sub_missing[@]} nao encontrados"
      if [ ${#sub_missing[@]} -gt 0 ]; then
        echo "    --- Lista de arquivos faltantes ---"
        for m in "${sub_missing[@]}"; do
          echo "      - $m"
        done
      fi
      echo ""
    done
  else
    # For other folders, collect all .md recursively
    echo "--- $folder/ ---"
    folder_files=()
    while IFS= read -r -d '' f; do
      folder_files+=("$f")
    done < <(find "$folder_path" -name "*.md" -type f -print0 2>/dev/null)
    
    folder_count=${#folder_files[@]}
    if [ "$folder_count" -eq 0 ]; then
      echo "  (vazio)"
      echo ""
      continue
    fi
    
    folder_in_acervo=0
    folder_missing=()
    
    for f in "${folder_files[@]}"; do
      bn=$(basename "$f")
      base_noext="${bn%.md}"
      OVERALL_MQTF=$((OVERALL_MQTF + 1))
      
      # Check exact match first, then without extension
      if [[ -n "${ACERVO_SET[$bn]:-}" ]]; then
        folder_in_acervo=$((folder_in_acervo + 1))
      elif [[ -n "${ACERVO_SET_NOEXT[$base_noext]:-}" ]]; then
        folder_in_acervo=$((folder_in_acervo + 1))
      else
         folder_missing+=("$bn")
      fi
    done
    
    OVERALL_IN_ACERVO=$((OVERALL_IN_ACERVO + folder_in_acervo))
    
    echo "  MQTF:     ${folder_count} arquivos"
    echo "  Acervo:   ${folder_in_acervo} encontrados"
    echo "  Faltam:   ${#folder_missing[@]} nao encontrados"
    if [ ${#folder_missing[@]} -gt 0 ]; then
      echo "  --- Lista de arquivos faltantes ---"
      for m in "${folder_missing[@]}"; do
        echo "    - $m"
      done
    fi
    echo ""
  fi
done

echo "============================================================"
echo "  RESUMO GERAL"
echo "============================================================"
echo "  Total MQTF (tematicos):  $OVERALL_MQTF"
echo "  Total Acervo:            $ACERVO_COUNT"
echo "  Em ambos (por nome):     $OVERALL_IN_ACERVO"
echo "  Apenas no MQTF:          $((OVERALL_MQTF - OVERALL_IN_ACERVO))"
echo "============================================================"
echo ""
echo "NOTA: A comparacao e feita por nome base do arquivo (.md)."
echo "      MQTF usa prefixos WTF_RES_, WTF_RAW_ enquanto o Acervo"
echo "      usa prefixos como ficha-, ifb-, resenha-."
echo "      Isso explica a baixa contagem de matches diretos."
echo "============================================================"
