# Projeto-Analise-basica25
Projeto de análise de dados populacionais da região de Maringá utilizando dados públicos do IBGE.   O projeto demonstra competências em: - Consumo de APIs REST - Limpeza e análise de dados com Python - Queries SQL - Visualização de dados - Relatórios em Excel
## 🎯 Objetivo

Analisar dados de população de 4 cidades da região de Maringá (Censo 2022) para extrair insights sobre a distribuição populacional urbana.

## 🛠️ Tecnologias Utilizadas

| Ferramenta | Uso |
|-----------|-----|
| **Python** | Lógica principal (Pandas, Requests, Matplotlib) |
| **SQL** | Consultas e filtros em banco de dados |
| **SQLite** | Armazenamento de dados |
| **Excel** | Relatório final |
| **IBGE API** | Fonte de dados públicos |

## 📊 O Que o Projeto Faz

1. **Coleta de Dados**: Requisição HTTP à API pública do IBGE
2. **Limpeza**: Extração de dados relevantes com Pandas
3. **Armazenamento**: Salvamento em banco SQLite
4. **Análise**: Query SQL para filtrar cidades com população > 50.000 hab
5. **Visualização**: Gráfico em Matplotlib (PNG)
6. **Relatório**: Exportação para Excel

## 📁 Arquivos do Projeto
```
projeto-maringa/
├── projeto_maringa.py          # Script principal
├── censo_maringa.db            # Banco de dados SQLite
├── grafico_populacao.png       # Gráfico gerado
├── Relatorio_Maringa.xlsx      # Relatório em Excel
└── README.md                   # Este arquivo
```

## 🚀 Como Executar

### Pré-requisitos
```bash
pip install requests pandas matplotlib openpyxl
```

### Rodar o projeto
```bash
python projeto_maringa.py
```

### Resultado esperado
```
Baixando dados do IBGE...
Limpando e organizando a tabela...
Salvando no Banco de Dados...
Cidades com mais de 50 mil habitantes (Via SQL):
   ...
Gerando Gráfico e Excel...
```

## 📈 Resultados Gerados

Após executar o script, você terá:

- **censo_maringa.db** - Banco de dados com tabela de população
- **grafico_populacao.png** - Gráfico em barras com as cidades
- **Relatorio_Maringa.xlsx** - Relatório formatado em Excel

## 💡 Skills Demonstrados

✅ **Python**: Manipulação de dados, requisições HTTP, visualização
✅ **SQL**: Queries com filtros (WHERE)
✅ **APIs REST**: Consumo de dados públicos
✅ **Análise de Dados**: Limpeza, transformação, agregação
✅ **Visualização**: Gráficos e relatórios



Desenvolvido como projeto de análise de dados para demonstração de competências em Python, SQL e análise de dados urbanos.
