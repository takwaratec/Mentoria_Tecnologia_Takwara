import re
import json

file_path = "01_TRIAGEM_BRUTA/WhatsApp Chat - Raízes - Grupo de Entrada - Junho 26/_chat.txt"

users = {}
current_user = None

pattern = re.compile(r'^\[\d{2}/\d{2}/\d{4} \d{2}:\d{2}:\d{2}\] ([^:]+): (.*)')

with open(file_path, 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
            
        match = pattern.match(line)
        if match:
            user = match.group(1).replace("~\u202f", "").strip()
            msg = match.group(2).strip()
            
            # Ignore system messages
            if "entrou usando o link do grupo" in msg or "mudou a descrição" in msg or "criou este grupo" in msg or "\u200e" in msg:
                continue
                
            current_user = user
            if user not in users:
                users[user] = []
            users[user].append(msg)
        else:
            if current_user:
                users[current_user].append(line)

profiles = {}
for user, msgs in users.items():
    full_text = " ".join(msgs)
    if len(full_text) > 100:  # heuristic for an introduction
        profiles[user] = full_text

with open("01_TRIAGEM_BRUTA/parsed_profiles.json", "w", encoding="utf-8") as out:
    json.dump(profiles, out, ensure_ascii=False, indent=4)

print(f"Extracted {len(profiles)} profiles.")
