# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 21:25:03 2024

@author: ana luiza sampaio
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar o dataset
df = pd.read_excel('stackoverflow_dataset.xlsx')

# Função para separar linguagens em listas
def split_languages(language_str):
    if pd.isnull(language_str):
        return []
    return language_str.split(';')

# Aplicar a função de separação na coluna 'LanguageWorkedWith'
df['LanguageWorkedWith_list'] = df['LanguageWorkedWith'].apply(split_languages)

# Criar colunas binárias (one-hot encoding) para cada linguagem em 'LanguageWorkedWith_list'
all_languages_worked = set([lang for sublist in df['LanguageWorkedWith_list'] for lang in sublist])

for language in all_languages_worked:
    df[f'WorkedWith_{language}'] = df['LanguageWorkedWith_list'].apply(lambda x: 1 if language in x else 0)

# Lista de linguagens para excluir
languages_to_exclude = [
    'WorkedWith_SQL', 'WorkedWith_HTML/CSS', 'WorkedWith_HTML', 
    'WorkedWith_CSS', 'WorkedWith_Bash/Shell/PowerShell', 
    'WorkedWith_Bash/Shell'
]

# Remover as colunas indesejadas
df = df.drop(columns=[lang for lang in languages_to_exclude if lang in df.columns])

# Agrupar por país e calcular a soma das colunas 'WorkedWith_{language}' para obter a contagem de uso por país
language_worked_counts_by_country = df.groupby('Country')[[f'WorkedWith_{lang}' for lang in all_languages_worked if f'WorkedWith_{lang}' not in languages_to_exclude]].sum()

# Adicionar uma coluna para o total de desenvolvedores por país
language_worked_counts_by_country['Total_Developers'] = language_worked_counts_by_country.sum(axis=1)

# Selecionar os 10 países com mais desenvolvedores
top_10_countries = language_worked_counts_by_country.nlargest(10, 'Total_Developers')

# Identificar a linguagem mais usada por país nos top 10
language_columns = [col for col in top_10_countries.columns if col.startswith('WorkedWith_')]
top_10_countries['Top_Language'] = top_10_countries[language_columns].idxmax(axis=1)
top_10_countries['Top_Language_Count'] = top_10_countries[language_columns].max(axis=1)

# Remover o prefixo 'WorkedWith_' para facilitar a leitura
top_10_countries['Top_Language'] = top_10_countries['Top_Language'].str.replace('WorkedWith_', '')

# Paleta de cores para as linguagens
unique_languages = top_10_countries['Top_Language'].unique()
colors = sns.color_palette("tab10", len(unique_languages))
color_map = dict(zip(unique_languages, colors))

# Plotar o gráfico de barras para os países e suas linguagens mais usadas
plt.figure(figsize=(12, 8))
bars = plt.barh(top_10_countries.index, 
                top_10_countries['Top_Language_Count'], 
                color=[color_map[lang] for lang in top_10_countries['Top_Language']])

plt.xlabel('Número de Desenvolvedores')
plt.ylabel('País')
plt.title('Linguagem Mais Usada por País (Top 10 Países)')
plt.grid(axis='x', linestyle='--', alpha=0.7)

# Adicionar a linguagem mais usada ao lado de cada barra
for index, (value, language) in enumerate(zip(top_10_countries['Top_Language_Count'], top_10_countries['Top_Language'])):
    plt.text(value + 1, index, language, va='center')

# Criar a legenda para as linguagens
plt.legend(handles=[plt.Line2D([0], [0], color=color_map[lang], lw=4) for lang in unique_languages], 
           labels=unique_languages, title="Linguagens", bbox_to_anchor=(1.05, 1), loc='upper left')

plt.tight_layout()
plt.show()
