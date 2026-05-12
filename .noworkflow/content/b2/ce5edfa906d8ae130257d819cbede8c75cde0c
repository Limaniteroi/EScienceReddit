import pandas as pd
import os

# ─── 1. LEITURA ───────────────────────────────────────────
print("Lendo o dataset...")
df = pd.read_csv("data/data_to_be_cleansed.csv")

print(f"Total de posts carregados: {len(df)}")
print(f"Colunas disponíveis: {list(df.columns)}")

# ─── 2. LIMPEZA ───────────────────────────────────────────
print("\nLimpando os dados...")

# Remove linhas sem texto e sem título
df = df.dropna(subset=["text", "title"])

# Remove duplicatas
df = df.drop_duplicates(subset=["text"])

# Remove posts com texto muito curto (menos de 20 caracteres)
df = df[df["text"].str.len() >= 20]

print(f"Total após limpeza: {len(df)}")

# ─── 3. SALVAMENTO ────────────────────────────────────────
print("\nSalvando dados limpos...")
os.makedirs("data", exist_ok=True)
df.to_csv("data/posts_limpos.csv", index=False)

print("Concluído! Arquivo salvo em data/posts_limpos.csv")