# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 21:25:03 2024

@author: ana luiza sampaio
"""

import pandas as pd
import matplotlib.pyplot as plt

# Carregar os resultados salvos do arquivo Excel
results_df = pd.read_excel("resultados_linguagens_predicao.xlsx")

# Ordenar o DataFrame por F1-Score Classe 1 (a principal métrica para a decisão, como indicado no objetivo)
results_df = results_df.sort_values(by="F1-Score Classe 1", ascending=False)

# Exibir as 10 linguagens com melhores F1-Score Classe 1, indicando a precisão para o ensino
top_languages_df = results_df.head(10)
print("Top 10 linguagens mais promissoras para o ensino:\n", top_languages_df)

# Visualização das linguagens com melhores métricas
plt.figure(figsize=(12, 8))
plt.barh(top_languages_df['Linguagem'], top_languages_df['F1-Score Classe 1'], color='skyblue', edgecolor='black')

# Configuração dos rótulos e título do gráfico
plt.xlabel("F1-Score Classe 1", fontsize=12)
plt.ylabel("Linguagem", fontsize=12)
plt.title("Top 10 Linguagens para se ensinar no futuro no Futuro", fontsize=14)
plt.gca().invert_yaxis()  # Inverter eixo para ter a melhor linguagem no topo

# Adicionar rótulos com valores de F1-Score ao lado das barras
for index, value in enumerate(top_languages_df['F1-Score Classe 1']):
    plt.text(value + 0.01, index, f"{value:.2f}", va='center', color='black')

plt.tight_layout()
plt.show()
