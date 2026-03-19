import requests    
import pandas as pd 
import sqlite3       
import matplotlib.pyplot as plt 

print("Baixando dados do IBGE...")
url = "https://apisidra.ibge.gov.br/values/t/4709/n6/4115200,4126256,4117602,4114302/v/93/p/2022"

resposta = requests.get(url)
dados_brutos = resposta.json()


print("Limpando e organizando a tabela...")
df = pd.DataFrame(dados_brutos)

df_limpo = df.iloc[1:][['D1N', 'V']].copy()
df_limpo.columns = ['cidade', 'populacao_2022']


df_limpo['populacao_2022'] = df_limpo['populacao_2022'].astype(int)

print(df_limpo)
print("\n3. Salvando no Banco de Dados...")


conexao = sqlite3.connect('censo_maringa.db')
df_limpo.to_sql('tabela_populacao', conexao, if_exists='replace', index=False)


query = "SELECT * FROM tabela_populacao WHERE populacao_2022 > 50000"
cidades_grandes = pd.read_sql(query, conexao)

print("\nCidades com mais de 50 mil habitantes (Via SQL):")
print(cidades_grandes)
print("\n4. Gerando Gráfico e Excel...")


df_grafico = df_limpo.sort_values(by='populacao_2022', ascending=False)


df_grafico.plot(x='cidade', y='populacao_2022', kind='bar', color='green', legend=False)
plt.title('População - Região de Maringá (Censo 2022)')
plt.ylabel('Habitantes')
plt.xticks(rotation=0) # Deixa os nomes das cidades retos
plt.tight_layout()


plt.savefig('grafico_populacao.png')
df_limpo.to_excel('Relatorio_Maringa.xlsx', index=False)

conexao.close()

