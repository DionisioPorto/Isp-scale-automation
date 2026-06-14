import pandas as pd

def carregar_tecnicos(caminho):
    return pd.read_csv(caminho)

def carregar_cidades(caminho):
    return pd.read_csv(caminho)