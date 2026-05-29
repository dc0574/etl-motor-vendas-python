# Motor de Processamento de Dados (ETL) em Python ⚙️📊

Um pipeline automatizado desenvolvido em **Python** para processamento de dados em rotinas de Back-End. Este projeto atua como um motor de consolidação que substitui o trabalho manual em planilhas, extraindo indicadores de negócios de forma escalável e segura.

## 🎯 Objetivo do Projeto
Criar uma solução autônoma para ler bases de dados externas (CSVs), higienizar informações mal formatadas e aplicar regras de negócio sem intervenção humana, gerando um relatório executivo em tempo real.

## 🛠️ Tecnologias Utilizadas
* **Linguagem:** Python
* **Bibliotecas:** `csv` (Nativa)
* **Conceitos Aplicados:** Lógica de Back-End, Tratamento de Exceções, Manipulação de Arquivos (I/O), Estruturas de Repetição e Condicionais.

## 🚀 Como funciona o Motor
1. **Ingestão de Dados:** O script abre e faz a leitura de um arquivo bruto de vendas (`vendas.csv`).
2. **Higienização (Defesa):** O motor possui travas de segurança que identificam e ignoram linhas em branco, cabeçalhos perdidos ou dados corrompidos.
3. **Processamento:** Aplica uma regra de negócios predefinida (ex: meta de R$ 2.000,00 por cliente) e classifica cada operação.
4. **Agregação:** Consolida automaticamente o faturamento total e o volume de sucessos.

## 💻 Como executar
Certifique-se de ter o Python instalado. Clone o repositório e, no terminal, navegue até a pasta do projeto e execute:
```bash
python motor_dados.py
