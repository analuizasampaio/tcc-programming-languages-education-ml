# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 21:25:03 2024

@author: ana luiza sampaio
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
from sklearn.preprocessing import LabelEncoder
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline

# Carregar o dataset
df = pd.read_excel('stackoverflow_dataset.xlsx')

# Função para separar valores nas colunas de linguagens
def split_languages(language_str):
    if pd.isnull(language_str):
        return []
    return language_str.split(';')

# função de separação nas colunas 'LanguageWorkedWith' e 'LanguageDesireNextYear'
df['LanguageWorkedWith_list'] = df['LanguageWorkedWith'].apply(split_languages)
df['LanguageDesireNextYear_list'] = df['LanguageDesireNextYear'].apply(split_languages)

# Criar colunas binárias (one-hot encoding) para cada linguagem
all_languages_worked = set([lang for sublist in df['LanguageWorkedWith_list'] for lang in sublist])
all_languages_desire = set([lang for sublist in df['LanguageDesireNextYear_list'] for lang in sublist])

for language in all_languages_worked.union(all_languages_desire):
    df[f'WorkedWith_{language}'] = df['LanguageWorkedWith_list'].apply(lambda x: 1 if language in x else 0)
    df[f'DesireNextYear_{language}'] = df['LanguageDesireNextYear_list'].apply(lambda x: 1 if language in x else 0)

# Lista de linguagens para excluir da análise
languages_to_exclude = [
    'WorkedWith_SQL', 'WorkedWith_HTML/CSS', 'WorkedWith_HTML', 'WorkedWith_CSS',
    'WorkedWith_Bash/Shell/PowerShell', 'WorkedWith_Bash/Shell'
]
df = df.drop(columns=[lang for lang in languages_to_exclude if lang in df.columns])

# Identificar as 10 linguagens mais trabalhadas após remover as linguagens indesejadas
language_worked_counts = df[[col for col in df.columns if col.startswith('WorkedWith_')]].sum()
top_10_linguagens = language_worked_counts.nlargest(10).index

print("As 10 linguagens mais frequentes:")
print(top_10_linguagens)

# Pré-processamento de dados categóricos e preenchimento de valores ausentes
label_columns = df.select_dtypes(include=['object']).columns
le = LabelEncoder()
for col in label_columns:
    df[col] = le.fit_transform(df[col].astype(str))

# Configurar pipeline com imputação de valores ausentes e o modelo de classificação com pesos balanceados
pipeline = Pipeline([
    ('imputer', SimpleImputer(strategy='mean')),
    ('classifier', RandomForestClassifier(class_weight='balanced', random_state=42))
])

for language in top_10_linguagens:
    target_col = f'DesireNextYear_{language.replace("WorkedWith_", "")}'
    
    if target_col in df.columns:
        y = df[target_col]
        X = df.drop(columns=[target_col] + list(top_10_linguagens))  
        
        # Dividir dados em treinamento e teste
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        # Treinar o modelo
        pipeline.fit(X_train, y_train)
        
        # Fazer previsões e avaliar o modelo
        y_pred = pipeline.predict(X_test)
        
        print(f"\nResultados para a linguagem: {target_col.replace('DesireNextYear_', '')}")
        print("Acurácia do modelo:", accuracy_score(y_test, y_pred))
        print(classification_report(y_test, y_pred, zero_division=1))
    else:
        print(f"Coluna {target_col} não encontrada no dataset.")

