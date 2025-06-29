import pandas as pd
import requests
import os

# === CONFIGURAÇÕES ===
API_KEY = 'YOUR KEY'
INPUT_CSV = 'contracts.csv'
OUTPUT_DIR = 'contracts_sol'
NUM_CONTRACTS = 50  # quantidade que você quer baixar

# === PREPARAÇÃO ===
os.makedirs(OUTPUT_DIR, exist_ok=True)
df = pd.read_csv(INPUT_CSV)
addresses = df['address'].drop_duplicates().tolist()

# === FUNÇÃO PARA CONSULTAR API ===
def get_contract_source(address):
    url = f"https://api.etherscan.io/api?module=contract&action=getsourcecode&address={address}&apikey={API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data['status'] == '1' and data['result']:
            source_code = data['result'][0].get('SourceCode', '')
            contract_name = data['result'][0].get('ContractName', address)
            return source_code.strip(), contract_name
    return None, None

# === LOOP DE DOWNLOAD ===
downloaded = 0
for address in addresses:
    if downloaded >= NUM_CONTRACTS:
        break
    source, name = get_contract_source(address)
    if source:
        filename = f"{OUTPUT_DIR}/{name and address}.sol"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(source)
        print(f"[OK] Baixado: {name and address}")
        downloaded += 1
    else:
        print(f"[X] Não verificado: {address}")

print(f"\n✅ Download concluído. {downloaded} contratos salvos em '{OUTPUT_DIR}'")
