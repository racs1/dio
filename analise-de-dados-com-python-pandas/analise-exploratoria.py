#importando as bibliotecas
from turtle import title
from xml.dom import registerDOMImplementation
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use("seaborn")
#criando o df
df = pd.read_excel("C:/Users/ramor/Desktop/Adventureworks.xlsx")
#análises iniciais - 5 primeiras linhas
df.head()
#Pergunta 1 - Receita Total?
round(df["Valor Venda"].sum(),2)
#Pergunta 2 - Custo Total?
df["Custo Total"] = df["Custo Unitário"]*df["Quantidade"]
round(df["Custo Total"].sum(),2)
#Pergunta 3 - Lucro Total?
df["Lucro Total"] = df["Valor Venda"]-df["Custo Total"]
round(df["Lucro Total"].sum(),2)
#Pergunta 4 - Total de dias para envio de cada produto?
df["Prazo Entrega"] = df["Data Envio"]-df["Data Venda"]
#Pergunta 5 - Média do tempo de envio para cada marca de produto?
df["Prazo Entrega"].dtype
df["Prazo Entrega"] = df["Prazo Entrega"].dt.days
df["Prazo Entrega"].dtype
df["Prazo Entrega"].groupby(df["Marca"]).mean()
#Pergunta 6 - Lucro por ano E por marca?
df["Ano"] = df["Data Venda"].dt.year
pd.options.display.float_format = '{:20,.2f}'.format
df["Lucro Total"].groupby([df["Ano"], df["Marca"]]).sum()
df["Lucro Total"].groupby([df["Ano"], df["Marca"]]).sum().reset_index()
#Pergunta 7 - Total de produtos vendidos?
df["Quantidade"].sum()
df["Quantidade"].groupby(df["Produto"]).sum().sort_values(ascending=False).reset_index()
#Pergunta 8 - Total de Vendas apenas de 2009?
df[df["Ano"]==2009]["Valor Venda"].head()
df[df["Ano"]==2009]["Valor Venda"].groupby(df["Data Venda"].dt.month).sum()

#Pergunta 9 - Plots
#9.1 Gráfico Lucro Mensal em 2009
df[df["Ano"]==2009]["Valor Venda"].groupby(df["Data Venda"].dt.month).sum().plot(title="Lucro Mensal em 2009")
plt.xlabel("Mês")
plt.ylabel("Lucro")
#9.2 Gráfico Lucro por Marca em 2009
df[df["Ano"]==2009]["Lucro Total"].groupby(df["Marca"]).sum().plot.bar(title="Lucro por Marca em 2009")
plt.xlabel("Marca")
plt.ylabel("Lucro")
plt.xticks(rotation='horizontal')
#9.3 Gráfico Lucro por Classe em 2009
df[df["Ano"]==2009]["Lucro Total"].groupby(df["Classe"]).sum().plot.bar(title="Lucro por Classe em 2009")
plt.xlabel("Classe")
plt.ylabel("Lucro")
plt.xticks(rotation='horizontal')
#9.4 Gráfico Total de Produtos Vendidos por ano
df["Quantidade"].groupby(df["Produto"]).sum().sort_values(ascending=False).plot.barh(title="Total Produtos Vendidos")
plt.xlabel("Total")
plt.ylabel("Produto")
#9.5 Gráfico Lucro por ano
df["Lucro Total"].groupby(df["Ano"]).sum().sort_values(ascending=False).plot.bar(title="Lucro x Ano")
plt.xlabel("Lucro")
plt.ylabel("Ano")


