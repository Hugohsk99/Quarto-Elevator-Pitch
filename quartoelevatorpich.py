# Algoritmo que trata da esparsidade dos dados de qualidade da água da Lagoa de Maricá.

# Importação das bibliotecas necessárias
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Definição da semente para garantir a reprodutibilidade
np.random.seed(0)

# Geração de um conjunto de dados simulados
x = np.random.choice(365, 100, replace=False)  # Dias do ano escolhidos aleatoriamente
y = np.random.choice(range(100), 100, replace=True)  # Valores medidos de forma aleatória
valid_measurements = np.random.choice([True, False], 100, p=[0.85, 0.15])  # Probabilidade de medição válida

# Criação de um DataFrame com os dados gerados
df = pd.DataFrame({
    'Dia do Ano': x,
    'Valor Medido': y,
    'Valido': valid_measurements
})

# Separação dos dados em válidos e inválidos
dados_validos = df[df['Valido'] == True]
dados_invalidos = df[df['Valido'] == False]

# Explorando a esparsidade dos dados:
# A esparsidade implica em muitos valores ausentes, o que pode levar a um desempenho insatisfatório
# de algoritmos de busca que esperam dados densamente distribuídos.

# Otimização em dados esparsos:
# Utilizar estruturas de dados especializadas para acelerar a busca e minimizar o acesso a dados nulos,
# como tabelas de hash ou árvores de busca que podem pular grandes blocos de dados nulos.

# Desenvolvimento de Algoritmo
# Proposta: Utilização de um mapa de hash para armazenar apenas medições válidas.

# Implementação da minimização de acessos nulos
mapa_hash = {dia: valor for dia, valor in zip(dados_validos['Dia do Ano'], dados_validos['Valor Medido'])}

# Complexidade Temporal
# A complexidade temporal para busca no mapa de hash é O(1),
# o que é significativamente mais rápido que uma busca linear O(n).

# Implementação do algoritmo em Python
# Busca no mapa de hash para um dia específico
dia_consulta = 200
valor_medido = mapa_hash.get(dia_consulta, None)

# Visualização dos dados e da busca
plt.scatter(df['Dia do Ano'], df['Valor Medido'], color='blue', label='Medições', alpha=0.5)
plt.scatter(dados_validos['Dia do Ano'], dados_validos['Valor Medido'], color='green', label='Dados Válidos', alpha=0.7)
plt.scatter(dados_invalidos['Dia do Ano'], dados_invalidos['Valor Medido'], color='red', label='Pontos Inválidos', alpha=0.5)

if valor_medido is not None:
    plt.scatter(dia_consulta, valor_medido, color='red', label='Ponto de Busca', zorder=5)

plt.xlabel('Dias do Ano')
plt.ylabel('Valor Medido')
plt.title('Registro Espaçado de Medidas de Qualidade da Água da Lagoa de Maricá')
plt.legend()
plt.grid(True)
plt.show()

# Impressão do valor medido no dia da consulta
print(f"O valor medido no dia {dia_consulta} é: {valor_medido if valor_medido is not None else 'não encontrado'}")

# Markdown para apresentação

markdown_text = """
# Análise de Esparsidade em Dados de Qualidade da Água

![Registro Espaçado de Medidas de Qualidade da Água da Lagoa de Maricá](grafico.png)

Apresentamos um algoritmo otimizado para o tratamento de dados esparsos referentes à qualidade da água da Lagoa de Maricá.

## Metodologia

- **Geração de Dados Simulados**: Dados representando medições de qualidade da água ao longo de um ano.
- **Estratégia de Otimização**: Utilização de um mapa de hash para armazenar e acessar rapidamente apenas as medições válidas.
- **Complexidade Temporal**: O(1) para buscas, proporcionando uma eficiência significativa em comparação a buscas lineares simples O(n) ou buscas binárias O(log n), especialmente considerando a natureza esparsa dos dados.

## Análise de Complexidade

A utilização de estruturas de dados especializadas, como mapas de hash, demonstra ser uma abordagem poderosa para otimizar algoritmos que operam em conjuntos de dados com alta esparsidade. A complexidade sintótica, O(1) para buscas no mapa de hash, é significativamente mais eficiente do que O(n) para uma busca linear e O(log n) para uma busca binária.

Isso significa que, independentemente do tamanho do conjunto de dados, o tempo para encontrar um elemento é constante no mapa de hash. Por outro lado, a complexidade assintótica reflete o comportamento do algoritmo à medida que o conjunto de dados se aproxima de um tamanho infinito, garantindo que o desempenho não degrada com conjuntos de dados extremamente grandes.

A otimização sintótica e assintótica é crucial para conjuntos de dados grandes e esparsos como o apresentado, onde a maioria das medições pode não ser válida, e uma busca eficiente é essencial para o desempenho.

## Conclusão

A abordagem proposta é ideal para cenários onde o acesso rápido a dados válidos é primordial e onde os dados inválidos são comuns. A visualização dos resultados ajuda a destacar a eficiência da abordagem adotada, mostrando uma clara distinção entre dados válidos e inválidos e o sucesso na rápida localização de dados específicos em um conjunto de dados esparsos.

"""

path_to_readme = 'README.md'
with open(path_to_readme, 'w') as readme_file:
    readme_file.write(markdown_text)

path_to_readme

