from src.leitor import (
    carregar_tecnicos,
    carregar_cidades
)

from src.escalador import gerar_escala
from src.exportador import salvar_escala
from src.relatorio import gerar_relatorio


def main():

    tecnicos = carregar_tecnicos(
        "dados/tecnicos.csv"
    )

    cidades = carregar_cidades(
        "dados/cidades.csv"
    )

    escala, alertas = gerar_escala(
        tecnicos,
        cidades
    )

    salvar_escala(escala)

    gerar_relatorio(alertas)

    print("\nEscala gerada com sucesso!")


if __name__ == "__main__":
    main()