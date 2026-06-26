#!/usr/bin/env bash
# busca — wrapper para busca semântica vetorial
# Uso: ./busca "sua pergunta sobre os repositórios"
# Ex:  ./busca "PU vegetal aplicacoes bambu"
#      ./busca "banheiro seco saneamento ecologico"
#      ./busca "proposta FINEP orcamento"

cd /Users/fabiotakwara/Documents/GitHub/Mentoria_Tecnologia_Takwara
/Users/fabiotakwara/miniconda3/envs/whisper_env/bin/python3 \
  scripts/busca_vector.py buscar "$*"
