
# Segundo exemplo de manipulacao de dados Python Pandas veremos insercao de dados, remocao de colinas, merge e graficos
#autor: Rafael Almeida

from IPython.display import display 
import pandas as pd
import numpy as np


combustiveis_df= pd.read_excel('ca202102_20230207120945.xlsx')
IBG_df= pd.read_csv('ibge_num_habitantes_estimado.csv',sep=';')
combustiveis_df['Ativa']= True
display(combustiveis_df.head(10))

combustiveis_df['OBS']= ["MELHOR CIDADE" if municipio == 'SAO PAULO' else None for municipio in combustiveis_df['Municipio']]
display(combustiveis_df['Municipio', 'OBS'].loc(ccombustiveis_df['Municipio']))

# Por: Leandreo Rodrgues ( valeu leandro :) )
# Prencher uma coluna 'Valor de Venda' que verefica se o valor de venda for maior de 6.60 coloca a lable 'caro' se for abaixo 'barato'
combustiveis_df['Status Valor de Venda']= np.where(combustiveis_df['Valor de Venda']> 6.5, 'Caro' , 'Barato')
display(combustiveis_df[['Revenda','Valor de Venda','Status Valor de Venda']])

#Calcular postos por de gasolina habitantes temos na amostragem de combustiveis de nov/2021
IBG_df.rename(columns={'Estado': 'Estado Sigla'}, inplace=True)# .rename serve para mudar o nome de uma coluna/linha 
display(IBG_df)

#Fazer um marge de dois data frames
colunas=['RegiaoSigla', 'Nome da Rua', 'Numero Rua', 
         'Bairro', 'Cep', 'Produto', 'Data da Coleta', 'Valor de Venda',
         'Unidade de Medida', 'Bandeira', 'Ativo', 'Status do Valor de Venda']

merge_df= combustiveis_df.merge(IBG_df, how='inner', on=colunas)
display(merge_df)
print(merge_df.info())

#Destruir coluna completamente vazia (todas as linhas são nulas)
merge_df.dropna(axis='columns', inplace=True)
print(merge_df.info())
merge_df.drop(labels=colunas, axis=1, inplace=True)
print(merge_df.info())

# Remover as linhas duplicadas
merge_df.drop_duplicates(inplace=True)
display(merge_df.head(100))