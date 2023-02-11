#Vamos brincar de gráficos!!!
from IPython.display import display 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


combustiveis_df = pd.read_excel("ca202102_20230207120945.xlsx") #Coloca a bd em uma vareavel


plt.hist(combustiveis_df['Valor de Venda'])
#Vamos colocar um título no gráfico
plt.title("Preço dos combustíveis - Nov/2021")
#Rótulo horizontal e vertical
plt.xlabel("Preço (em reais)")
plt.ylabel("Quantidade de Coletas")

#Traça a linha vermelha tracejada com o preço médio
plt.axvline(combustiveis_df['Valor de Venda'].mean(), color='red', linestyle='dashed', linewidth=5)


#"Plota" o gráfico
plt.show()

#Visualização do consumo médio
c_mean = combustiveis_df['Valor de Venda'].groupby(by=combustiveis_df['Produto']).mean()
display(c_mean)

#Vou definir a área do gráfico
plt.figure(figsize=(7,5))

#Plotar o gráfico
c_mean.plot(
    kind="barh",
    xlabel="Tipo de Combustível",
    ylabel="Preço reais/litro",
    color="red"
)

#Grid
plt.grid()

#Exibe
plt.show()

#Vou definir a área do gráfico
plt.figure(figsize=(7,5))

#Plotar o gráfico
c_mean.plot(
    kind="barh",
    xlabel="Tipo de Combustível",
    ylabel="Preço reais/litro",
    title="Média de preços por combustível",
    color="red",
    alpha=0.3
)

#Grid
plt.grid()

#Remover as linhas superior e lateral direita do gráfico 
sns.despine()

#Exibe
plt.show()