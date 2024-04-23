# A explicação sobre o impacto da esparsidade dos dados de qualidade da água e estratégias para otimização da busca em dados esparsos.
# O desenvolvimento de um algoritmo teórico que utilize uma estrutura de dados especializada para minimizar o acesso a dados nulos e acelerar a localização de registros válidos.
# Implementação de uma técnica para minimização de acessos nulos durante a busca.
# Análise da complexidade temporal do algoritmo otimizado em comparação com uma busca linear simples e uma pesquisa binária, além de condições de preferência para quando o algoritmo otimizado é a melhor escolha.
# Codificação do algoritmo em Python e visualização dos dados e da busca.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

# Inicialização do gerador de números aleatórios
np.random.seed(0)

# Geração de um conjunto de dados aleatórios e esparsos simulando as medições
x = np.random.choice(365, 100, replace=False)  # Dias aleatórios do ano
y = np.random.choice(range(100), 100, replace=True)  # Valores medidos aleatórios
valid_measurements = np.random.choice([True, False], 100, p=[0.85, 0.15])  # 85% de chance da medição ser válida

# Criação de um DataFrame do pandas a partir dos dados simulados
df = pd.DataFrame({
    'Dia do Ano': x,
    'Valor Medido': y,
    'Valido': valid_measurements
})

# Filtragem dos dados para separar medições válidas das inválidas
dados_validos = df[df['Valido'] == True]
dados_invalidos = df[df['Valido'] == False]

# Tarefa 1.1: O impacto da esparsidade é que muitos algoritmos de busca tradicionais podem ter desempenho ruim devido à
# necessidade de ignorar muitos pontos de dados nulos ou inválidos, que podem estar distribuídos aleatoriamente pelo conjunto de dados.

# Tarefa 1.2: Métodos para otimização podem incluir o uso de indexação para localizar rapidamente dados não nulos ou o uso de árvores de busca especializadas.

# Tarefa 2.1: Teorizamos um algoritmo que utiliza um mapa de hash para armazenar apenas medições válidas para minimizar o acesso a dados nulos.

# Tarefa 2.2: Implementação de uma técnica que permita a minimização do acesso a dados nulos durante a busca.
# Aqui, filtramos as medições inválidas.
mapa_hash = {dia: valor for dia, valor in zip(dados_validos['Dia do Ano'], dados_validos['Valor Medido'])}

# Tarefa 3.1: Análise da complexidade temporal.
# A complexidade temporal do nosso algoritmo teorizado seria O(1) para consultas no mapa de hash, o que é muito mais rápido
# do que uma busca linear simples O(n) e comparável à busca binária O(log n) no melhor cenário.

# Tarefa 4.1: Implementação do algoritmo em Python usando dados simulados.
# Para demonstração, vamos apenas mostrar um exemplo de consulta no mapa de hash.
dia_consulta = 200
valor_medido = mapa_hash.get(dia_consulta, None)  # Isso terá complexidade O(1)

# Tarefa 4.2: Visualização dos dados e da busca.
# Plotagem dos dados originais esparsos
plt.scatter(df['Dia do Ano'], df['Valor Medido'], color='blue', label='Medições', alpha=0.5)
# Plotagem dos pontos de dados válidos em verde
plt.scatter(dados_validos['Dia do Ano'], dados_validos['Valor Medido'], color='green', label='Dados Válidos', alpha=0.7)
# Plotagem dos pontos de dados inválidos em vermelho
plt.scatter(dados_invalidos['Dia do Ano'], dados_invalidos['Valor Medido'], color='red', label='Pontos Inválidos', alpha=0.5)
# Destaque do valor de consulta, se existir
if valor_medido is not None:
    plt.scatter(dia_consulta, valor_medido, color='red', label='Ponto de Busca', zorder=5)
plt.xlabel('Dias do Ano')
plt.ylabel('Valor Medido')
plt.title('Registro Espaçado de Medidas de Qualidade da Água da Lagoa de Maricá')
plt.legend()
plt.grid(True)
plt.show()

# Impressão do valor medido no dia de consulta
print(f"O valor medido no dia {dia_consulta} é: {valor_medido}")
