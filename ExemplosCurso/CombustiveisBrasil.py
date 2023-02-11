#Primeiro de manipulacao de dados usando python pandas
#autor: Rafael Almeida da Silva

from IPython.display import display 
import pandas as pd

combustiveis_df = pd.read_excel("ca202102_20230207120945.xlsx") #Coloca a bd em uma vareavel
ca_df= combustiveis_df[['Revenda', 'Municipio', 'Produto','Valor de Venda']]#craicao de um novo df com as tres colnas especificadas
GASOLINA_df= ca_df.loc[ca_df['Produto'] == 'GASOLINA']# Exibe a linha expecificada
Ethanol_Indaituba_Df = (ca_df.loc[(ca_df['Produto']== 'ETANOL') & (ca_df['Municipio']=='INDAIATUBA')]) # Loc com multiplos condicoes
Meadia_Gasolina_Mocca = combustiveis_df.loc[(combustiveis_df['Bairro'] == 'MOOCA') &
                                                 (combustiveis_df['Municipio'] == 'SAO PAULO')
                                                   & ((combustiveis_df['Produto']== 'GASOLINA') | (combustiveis_df['Produto']== 'GASOLINA ADITIVADA')),['Valor de Venda']].mean()

#Funcoes basicas do panda
display(combustiveis_df.head(15)) # serve para mostrar o n de linhas
display(combustiveis_df.shape) # serve para mostar o numero de colnas e linhas
display(combustiveis_df.info) #Quais sao as colunas e os tipos de dados que tem
display(combustiveis_df.describe()) # mostra as estatisticas basicas
display(combustiveis_df['Revenda'].head(11)) #Filtrar por uma coluna

#Funcao LOC pandas
display(ca_df.head(10)) 
display(ca_df.loc[3])
display(ca_df.loc[9:19])# Filtragem por intervalo 
display(Ethanol_Indaituba_Df.sort_values(by='Valor de Venda', inplace=True))# Inplace serve para quardar o sort quando ele for mostrado, caso nao seja colocado o sort sera mostrado fora de ordem

display(Meadia_Gasolina_Mocca)

Media_Combustivel_BRA= ca_df[['Produto', 'Valor de Venda']].groupby(by='Produto').mean().round(2)# groupby faz um agrupamento devarias linhas e junta em uma so. Nesse caso resume todo o valor de produto#display(Media_Combustivel_BRA)

display(GASOLINA_df[['Revenda', 'Municipio','Valor de Venda']].max())

combustiveis_df['Ativa']= True # adicao de uma coluna 

print(combustiveis_df.info())
display(combustiveis_df.head(10))

#Ethanol_Indaituba_Df.to_excel('EthanolIndaituba.xlsx', sheet_name='Ethanol em Indaituba')# .to_excel serve para converter um data frame em um formato expecificado