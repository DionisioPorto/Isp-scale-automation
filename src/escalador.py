def gerar_escala(df):

    disponiveis = df[
        df["disponivel"] == "Sim"
    ]

    escala = []

    for _, tecnico in disponiveis.iterrows():

        escala.append({
            "cidade": tecnico["cidade"],
            "tecnico": tecnico["nome"]
        })

    return escala