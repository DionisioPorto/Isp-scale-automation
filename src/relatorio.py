def gerar_relatorio(alertas):

    print("\n===== RELATÓRIO =====\n")

    if not alertas:
        print("Nenhum problema encontrado.")
        return

    for alerta in alertas:
        print(alerta)