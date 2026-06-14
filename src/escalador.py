def gerar_escala(tecnicos, cidades):

    escala = []
    alertas = []

    disponiveis = tecnicos[
        tecnicos["disponivel"] == "Sim"
    ]

    for _, cidade in cidades.iterrows():

        nome_cidade = cidade["cidade"]
        cobertura = cidade["cobertura"]

        tecnicos_cidade = disponiveis[
            disponiveis["cidade_base"] == nome_cidade
        ]

        quantidade_disponivel = len(tecnicos_cidade)

        if quantidade_disponivel < cobertura:

            faltando = cobertura - quantidade_disponivel

            alertas.append(
                f"{nome_cidade}: faltam {faltando} técnico(s)"
            )

        selecionados = tecnicos_cidade.head(cobertura)

        for _, tecnico in selecionados.iterrows():

            escala.append({
                "cidade": nome_cidade,
                "tecnico": tecnico["nome"]
            })

    return escala, alertas