import pandas as pd


def salvar_escala(escala):

    df = pd.DataFrame(escala)

    df.to_csv(
        "dados/escala_gerada.csv",
        index=False
    )