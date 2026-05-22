import os
from pathlib import Path
from shutil import copyfile

import certifi
import pandas as pd


os.environ.setdefault("SSL_CERT_FILE", certifi.where())
os.environ.setdefault("REQUESTS_CA_BUNDLE", certifi.where())

import kagglehub


DATASET = "neelghoshal/reddit-mental-health-data"
DATA_DIR = Path("data")
REQUIRED_COLUMNS = {"text", "title", "target"}


def tem_colunas_obrigatorias(arquivo):
    try:
        if arquivo.suffix == ".xlsx":
            df = pd.read_excel(arquivo, nrows=5)
        else:
            df = pd.read_csv(arquivo, nrows=5)
    except Exception:
        return False

    return REQUIRED_COLUMNS.issubset(df.columns)


def encontrar_arquivo_baixado(pasta_dataset):
    candidatos = list(pasta_dataset.rglob("*.csv")) + list(pasta_dataset.rglob("*.xlsx"))
    for arquivo in candidatos:
        if tem_colunas_obrigatorias(arquivo):
            return arquivo

    raise FileNotFoundError(
        "Nao encontrei um CSV ou XLSX com as colunas text, title e target "
        f"depois de baixar o dataset {DATASET}."
    )


def padronizar_nome(arquivo):
    destino = DATA_DIR / f"data_to_be_cleansed{arquivo.suffix}"
    if arquivo.resolve() != destino.resolve():
        copyfile(arquivo, destino)
    return destino


def main():
    DATA_DIR.mkdir(exist_ok=True)

    print(f"Baixando dataset do Kaggle: {DATASET}")
    pasta_dataset = Path(kagglehub.dataset_download(DATASET))
    print(f"Path to dataset files: {pasta_dataset}")

    arquivo = encontrar_arquivo_baixado(pasta_dataset)
    destino = padronizar_nome(arquivo)

    print(f"Dataset pronto em: {destino}")


if __name__ == "__main__":
    try:
        main()
    except Exception as erro:
        raise SystemExit(f"Erro ao baixar dataset: {erro}")
