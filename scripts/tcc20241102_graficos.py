# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 21:25:03 2024

@author: ana luiza sampaio
"""

import pandas as pd
import matplotlib.pyplot as plt

# Carregar os resultados salvos do arquivo Excel
results_df = pd.read_excel("resultados_linguagens_predicao.xlsx")

# Ordenar o DataFrame por F1-Score Classe 1
top_languages_f1 = results_df.sort_values(by="F1-Score Classe 1", ascending=False).head(10)
top_languages_accuracy = results_df.sort_values(by="Acurácia", ascending=False).head(10)
top_languages_precision = results_df.sort_values(by="Precisão Classe 1", ascending=False).head(10)

# Configurações para melhorar a visualização
fig, axes = plt.subplots(nrows=3, ncols=1, figsize=(12, 18))
fig.suptitle("Top 10 Linguagens com Melhores Métricas Preditivas para Ensino", fontsize=16, weight='bold')

# Gráfico para F1-Score Classe 1
axes[0].barh(top_languages_f1['Linguagem'], top_languages_f1['F1-Score Classe 1'], color='cornflowerblue', edgecolor='black')
axes[0].set_xlabel("F1-Score Classe 1", fontsize=12)
axes[0].set_ylabel("Linguagem", fontsize=12)
axes[0].set_title("Top 10 Linguagens por F1-Score Classe 1", fontsize=14)
axes[0].invert_yaxis()
for index, value in enumerate(top_languages_f1['F1-Score Classe 1']):
    axes[0].text(value + 0.01, index, f"{value:.2f}", va='center', color='black')

# Gráfico para Acurácia
axes[1].barh(top_languages_accuracy['Linguagem'], top_languages_accuracy['Acurácia'], color='lightgreen', edgecolor='black')
axes[1].set_xlabel("Acurácia", fontsize=12)
axes[1].set_ylabel("Linguagem", fontsize=12)
axes[1].set_title("Top 10 Linguagens por Acurácia", fontsize=14)
axes[1].invert_yaxis()
for index, value in enumerate(top_languages_accuracy['Acurácia']):
    axes[1].text(value + 0.01, index, f"{value:.2f}", va='center', color='black')

# Gráfico para Precisão Classe 1
axes[2].barh(top_languages_precision['Linguagem'], top_languages_precision['Precisão Classe 1'], color='salmon', edgecolor='black')
axes[2].set_xlabel("Precisão Classe 1", fontsize=12)
axes[2].set_ylabel("Linguagem", fontsize=12)
axes[2].set_title("Top 10 Linguagens por Precisão Classe 1", fontsize=14)
axes[2].invert_yaxis()
for index, value in enumerate(top_languages_precision['Precisão Classe 1']):
    axes[2].text(value + 0.01, index, f"{value:.2f}", va='center', color='black')

# Ajustar o layout e exibir os gráficos
plt.tight_layout(rect=[0, 0, 1, 0.96])  
plt.show()

