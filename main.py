from src.leitor import carregar_tecnicos
from src.escalador import gerar_escala
from src.exportador import salvar_escala


def main():

    tecnicos = carregar_tecnicos(
        "dados/tecnicos.csv"
    )

    escala = gerar_escala(
        tecnicos
    )

    salvar_escala(
        escala
    )

    print("Escala gerada com sucesso!")


if __name__ == "__main__":
    main()