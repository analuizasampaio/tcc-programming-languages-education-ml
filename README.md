
# Linguagens de Programação - Análise e Predição 🚀

## Descrição do Projeto 📋

Este projeto tem como objetivo analisar a popularidade e a evolução das linguagens de programação ao longo dos anos, com base em dados do StackOverflow e GitHub. Além disso, o projeto utiliza modelos preditivos para identificar linguagens promissoras para aprendizado e ensino no futuro.

---

## 📜 Tabela de Conteúdos

<!--ts-->
   * [Sobre](##Sobre)
   * [Tabela de Conteúdo](#tabela-de-conteúdo)
   * [Instalação](#instalação)
   * [Como Usar](#como-usar)
      * [Pré-requisitos](#pré-requisitos)
      * [Exemplo de Execução](#exemplo-de-execução)
   * [Resultados](#resultados)
   * [Tecnologias](#tecnologias)
   * [Autor](#autor)
<!--te-->

---

## Sobre 💡

O projeto utiliza dados de desenvolvedores para identificar as linguagens mais utilizadas por países e as mais promissoras para o futuro. Também inclui análises gráficas e comparativas de tendências baseadas em dados históricos.

---

## Instalação ⚙️

1. Clone o repositório:
   ```bash
   git clone https://github.com/seuusuario/repositorio.git
   ```

2. Instale os pacotes necessários:
   ```bash
   pip install -r requirements.txt
   ```

3. Certifique-se de ter o arquivo de dados `stackoverflow_dataset.xlsx` na mesma pasta dos scripts.

---

## Como Usar 🚀

### Pré-requisitos

- Python 3.9+
- Bibliotecas necessárias (instaladas pelo `requirements.txt`)

### Exemplo de Execução

1. **Análise de Linguagens por País**:
   Execute o script `tcc20241118_paises.py` para gerar gráficos sobre as linguagens mais populares por país.
   ```bash
   python tcc20241118_paises.py
   ```

2. **Coleta de Dados do GitHub**:
   Use `tcc20241118_github.py` para analisar linguagens populares nos repositórios mais estrelados.
   ```bash
   python tcc20241118_github.py
   ```

3. **Modelos Preditivos**:
   Avalie linguagens promissoras para ensino com `tcc20241102_preditiva.py`.
   ```bash
   python tcc20241102_preditiva.py
   ```

---

## Resultados 📊

### Linguagens Mais Usadas por País 🌍
![Top Linguagens por País](top_languages_by_country.png)

### Predições de Ensino 🧑‍🏫
Gráficos de análise e F1-Score das linguagens mais promissoras.

| Linguagem     | F1-Score | Precisão | Recall |
|---------------|----------|----------|--------|
| Python        | 0.95     | 0.93     | 0.97   |
| JavaScript    | 0.92     | 0.90     | 0.94   |

---

## Tecnologias 🛠️

- **Python** 🐍
- **Pandas**
- **Matplotlib**
- **Seaborn**
- **Scikit-Learn**
- **API GitHub**

---

## Autor ✍️

Feito por Ana Luiza Sampaio.

[![LinkedIn Badge](https://img.shields.io/badge/-Ana%20Luiza%20Sampaio-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/analuizasampaio/)](https://www.linkedin.com/in/analuizasampaio/)

---

