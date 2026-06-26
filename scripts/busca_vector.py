#!/usr/bin/env python3
"""Indexador semântico local — Varre os repositórios .md e cria busca vetorial."""

import os
import sys
import glob
import chromadb
from chromadb.utils import embedding_functions

# Repositórios para indexar
REPOS = {
    "Mentoria": "/Users/fabiotakwara/Documents/GitHub/Mentoria_Tecnologia_Takwara",
    "ECOSALA": "/Users/fabiotakwara/Documents/GitHub/ECOSALA",
    "Vaga_Lumen": "/Users/fabiotakwara/Documents/GitHub/fundo-vaga-lumen-2026",
    "MST_Mario_Lago": "/Users/fabiotakwara/Documents/MST-IFSP-MArio_Lago",
    "Acervo_Cientifico": "/Users/fabiotakwara/Documents/GitHub/Analises e escrita científica",
}

DB_DIR = os.path.expanduser("~/.hermes/vector_db")
COLLECTION_NAME = "takwara_repos"

def indexar():
    """Varre todos os .md e cria o banco vetorial."""
    os.makedirs(DB_DIR, exist_ok=True)
    
    client = chromadb.PersistentClient(path=DB_DIR)
    
    # Tenta pegar collection existente ou cria nova
    try:
        collection = client.get_collection(COLLECTION_NAME)
        print(f"🗑️  Collection existente encontrada. Vou recriar.")
        client.delete_collection(COLLECTION_NAME)
    except:
        pass
    
    # Usa embedding function padrão (all-MiniLM-L6-v2 via ONNX)
    collection = client.create_collection(
        name=COLLECTION_NAME,
        metadata={"hnsw:space": "cosine"}
    )
    
    docs = []
    metadatas = []
    ids = []
    
    for repo_name, repo_path in REPOS.items():
        if not os.path.exists(repo_path):
            print(f"  ⚠️ {repo_name}: caminho não encontrado, pulando")
            continue
        
        md_files = glob.glob(os.path.join(repo_path, "**/*.md"), recursive=True)
        # Filtra site/ e TRIAGEM-BRUTA/
        md_files = [f for f in md_files if "/site/" not in f and "/TRIAGEM-BRUTA/" not in f and "/TRIAGEM_BRUTA/" not in f and ".git/" not in f]
        
        print(f"  📂 {repo_name}: {len(md_files)} arquivos .md")
        
        for fpath in md_files:
            try:
                with open(fpath, 'r', encoding='utf-8', errors='replace') as f:
                    content = f.read()
                
                if len(content.strip()) < 50:  # Pula arquivos vazios
                    continue
                
                # Gera ID único
                fname = os.path.basename(fpath)
                relpath = os.path.relpath(fpath, repo_path)
                doc_id = f"{repo_name}::{relpath}"
                
                docs.append(content[:5000])  # Limita a 5000 chars
                metadatas.append({
                    "repo": repo_name,
                    "arquivo": fname,
                    "caminho": relpath,
                    "tamanho": len(content)
                })
                ids.append(doc_id)
                
            except Exception as e:
                print(f"    ⚠️ Erro lendo {fpath}: {e}")
    
    # Adiciona em lotes (chromadb tem limite de ~100 por batch)
    batch_size = 100
    for i in range(0, len(docs), batch_size):
        batch_end = min(i + batch_size, len(docs))
        collection.add(
            documents=docs[i:batch_end],
            metadatas=metadatas[i:batch_end],
            ids=ids[i:batch_end]
        )
        print(f"    → Indexados {batch_end}/{len(docs)}")
    
    print(f"\n✅ Indexação concluída: {len(docs)} documentos em {len(REPOS)} repositórios")
    print(f"📁 Banco em: {DB_DIR}")


def buscar(consulta, n_resultados=10):
    """Busca semântica nos documentos indexados."""
    client = chromadb.PersistentClient(path=DB_DIR)
    
    try:
        collection = client.get_collection(COLLECTION_NAME)
    except:
        print("❌ Nenhum índice encontrado. Execute o indexador primeiro.")
        return
    
    results = collection.query(
        query_texts=[consulta],
        n_results=n_resultados
    )
    
    print(f"\n🔍 Busca: '{consulta}'")
    print(f"{'='*60}")
    
    for i, (doc, metadata, distance) in enumerate(zip(
        results['documents'][0],
        results['metadatas'][0],
        results['distances'][0]
    )):
        score = 1 - distance  # converte distância em similaridade
        print(f"\n--- Resultado {i+1} (similaridade: {score:.2%}) ---")
        print(f"📂 {metadata['repo']}/{metadata['caminho']}")
        print(f"📄 {doc[:300]}...")
    
    print(f"\n{'-'*60}")


def menu():
    """Menu interativo."""
    while True:
        print("\n" + "="*50)
        print("🔍 BUSCA SEMÂNTICA TAKWARA")
        print("="*50)
        print("1. Indexar todos os repositórios")
        print("2. Buscar")
        print("3. Sair")
        
        op = input("\nOpção: ").strip()
        
        if op == "1":
            indexar()
        elif op == "2":
            q = input("\nPergunta/busca: ").strip()
            if q:
                buscar(q)
        elif op == "3":
            break
        else:
            print("Opção inválida")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == "indexar":
            indexar()
        elif sys.argv[1] == "buscar":
            if len(sys.argv) > 2:
                buscar(" ".join(sys.argv[2:]))
            else:
                print("Uso: python3 busca_vector.py buscar 'sua pergunta aqui'")
        elif sys.argv[1] == "menu":
            menu()
    else:
        menu()
