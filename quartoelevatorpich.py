# Bibliotecas necessárias
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Definindo a semente para reprodução dos resultados
np.random.seed(0)

# Geração de um conjunto de dados simulando as medições de qualidade da água
# com uma quantidade significativa de dados ausentes (espaços vazios)
x = np.random.choice(365, 100, replace=False)  # Dias aleatórios do ano
y = np.random.choice(range(100), 100, replace=True)  # Valores medidos aleatoriamente
valid_measurements = np.random.choice(
    [True, False], 100, p=[0.85, 0.15]
)  # Probabilidade das medições serem válidas

# Criando DataFrame com os dados simulados
df = pd.DataFrame({"Dia do Ano": x, "Valor Medido": y, "Valido": valid_measurements})

# Separação dos dados em válidos e inválidos para facilitar a análise
dados_validos = df[df["Valido"] == True]
dados_invalidos = df[df["Valido"] == False]

# -------------------
# Detalhando Tarefas para análise
# -------------------

# O impacto da esparsidade é evidenciado pela presença de muitos dados inválidos (representados por 'x' vermelhos no gráfico).
# Isso afeta a eficiência de algoritmos de busca tradicionais, que teriam que percorrer o conjunto de dados completo,
# aumentando o tempo de busca desnecessariamente.

# Para otimizar a busca em dados esparsos, podemos utilizar métodos como:
# 1. Indexação para localizar rapidamente entradas não nulas.
# 2. Estruturas de dados especializadas como árvores de busca balanceadas ou tabelas de hash que minimizam o acesso a dados nulos.

# Desenvolvimento do algoritmo:
# Propomos um algoritmo que utiliza uma tabela de hash (mapa_hash) para armazenar apenas medições válidas,
# reduzindo a complexidade temporal das operações de busca.

# Implementação da minimização de acesso a dados nulos:
# Filtramos o conjunto de dados original para criar um mapa de hash contendo apenas as medições válidas.
mapa_hash = {
    dia: valor
    for dia, valor in zip(dados_validos["Dia do Ano"], dados_validos["Valor Medido"])
}

# Análise da complexidade temporal:
# As buscas no mapa de hash têm complexidade O(1), o que é muito mais eficiente do que uma busca linear simples O(n)
# e comparável à busca binária O(log n) em termos de complexidade média.

# Implementação em Python:
# Para o dia de consulta 200, buscamos o valor medido usando o mapa de hash, que é uma operação de tempo constante O(1).
dia_consulta = 200
valor_medido = mapa_hash.get(dia_consulta, None)

# Visualização dos dados e da busca:
# Representamos graficamente os dados simulados, destacando os pontos válidos e inválidos,
# e ilustramos a busca eficiente no mapa de hash.

# Plotagem dos dados esparsos com pontos válidos e inválidos
plt.scatter(
    df["Dia do Ano"], df["Valor Medido"], color="blue", label="Medições", alpha=0.5
)
plt.scatter(
    dados_validos["Dia do Ano"],
    dados_validos["Valor Medido"],
    color="green",
    label="Dados Válidos",
    alpha=0.7,
)
plt.scatter(
    dados_invalidos["Dia do Ano"],
    dados_invalidos["Valor Medido"],
    color="red",
    label="Pontos Inválidos",
    alpha=0.5,
)

# Se um valor medido foi encontrado no dia de consulta, destacamos este ponto
if valor_medido is not None:
    plt.scatter(
        dia_consulta, valor_medido, color="red", label="Ponto de Busca", zorder=5
    )

# Configurações finais do gráfico
plt.xlabel("Dias do Ano")
plt.ylabel("Valor Medido")
plt.title("Registro Espaçado de Medidas de Qualidade da Água da Lagoa de Maricá")
plt.legend()
plt.grid(True)
plt.show()

# Conclusão roteirizada do algoritmo:
# # "Implemenração de um algoritmo eficiente para tratar a esparsidade dos dados de qualidade da água da Lagoa de Maricá. Utilizando uma tabela de hash, conseguimos armazenar apenas as medições válidas, permitindo assim uma busca rápida e eficaz, com uma complexidade de tempo constante O(1) para consultas. Isso demonstra uma melhoria significativa em relação às buscas lineares simples, especialmente quando lidamos com grandes conjuntos de dados. A visualização dos dados nos oferece uma compreensão clara da distribuição das medições e da eficiência do algoritmo proposto, ressaltando a utilidade de estruturas de dados especializadas no tratamento de dados esparsos. Este algoritmo é particularmente útil em cenários onde a velocidade de recuperação dos dados é crucial e os dados inválidos são frequentes."
