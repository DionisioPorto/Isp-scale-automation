# Isp-scale-automation
# ISP Scale Automation

Automação desenvolvida em Python para auxiliar na distribuição de técnicos em operações de provedores de internet (ISP), validando cobertura mínima por cidade e identificando déficits operacionais.

## Objetivo

Reduzir o tempo gasto na criação manual de escalas operacionais e fornecer alertas quando a quantidade de técnicos disponíveis não atende a cobertura necessária de cada região.

## Funcionalidades

- Leitura de dados a partir de arquivos CSV
- Validação de disponibilidade dos técnicos
- Distribuição automática por cidade
- Verificação de cobertura mínima
- Geração de alertas para regiões com déficit operacional
- Exportação da escala gerada para CSV

## Tecnologias Utilizadas

- Python 3
- Pandas
- OpenPyXL
- Git
- GitHub

## Estrutura do Projeto

```text
isp-scale-automation/
│
├── dados/
│   ├── tecnicos.csv
│   ├── cidades.csv
│   └── escala_gerada.csv
│
├── src/
│   ├── leitor.py
│   ├── escalador.py
│   ├── exportador.py
│   └── relatorio.py
│
├── main.py
├── requirements.txt
└── README.md
```

## Exemplo de Entrada

### Técnicos

| Nome | Cidade Base | Disponível |
|--------|--------|--------|
| João | Curitiba | Sim |
| Lucas | Curitiba | Sim |
| Maria | Londrina | Sim |
| Pedro | Maringá | Sim |

### Cobertura

| Cidade | Cobertura |
|----------|----------|
| Curitiba | 2 |
| Londrina | 1 |
| Maringá | 2 |

## Exemplo de Saída

```text
===== RELATÓRIO =====

Maringá: faltam 1 técnico(s)

Escala gerada com sucesso!
```

## Como Executar

Clone o repositório:

```bash
git clone https://github.com/DionisioPorto/Isp-scale-automation.git
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute:

```bash
python main.py
```

## Melhorias Futuras

- Realocação automática entre cidades
- Interface Web com Flask
- Dashboard operacional
- Integração com Excel
- Exportação de relatórios em PDF

## Autor

Dionísio Porto

Profissional de Suporte Técnico, Infraestrutura e Automação de Processos.
