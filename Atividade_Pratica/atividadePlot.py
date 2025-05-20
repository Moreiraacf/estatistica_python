import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)


df = pd.read_csv(r'C:\Users\Usuário\Documents\ProjetoPy\Atividade_Pratica\ecommerce_estatistica.csv')

print(df.head()) # Exibe as primeiras linhas do DataFrame
print(df.isnull().sum().sum()) 

x = df['Qtd_Vendidos'].value_counts().index
y = df['Qtd_Vendidos_Cod'].value_counts().values

# # Histograma
plt.figure(figsize=(10, 6))
plt.hist(df['Qtd_Vendidos'], bins=15, color='blue', alpha=0.7)
plt.title('Histograma da Quantidade de Produtos Vendidos')
plt.xlabel('Produtos Vendidos')
plt.ylabel('Quantidade')
plt.grid(True)
plt.show()

# Dispersão
plt.figure(figsize=(10, 6))
plt.scatter(df['Marca_Cod'], df['Marca_Freq'], alpha=0.5)
plt.title('Gráfico de Dispersão - Marca vs Frequência')
plt.xlabel('Marca')
plt.ylabel('Frequência')
plt.show()

# Mapa de Calor
df_corr = df[['Marca_Cod','Marca_Freq', 'Nota_MinMax', 'N_Avaliações_MinMax', 'Qtd_Vendidos_Cod', 
              'Temporada_Cod', 'Marca_Freq']].corr()

plt.figure(figsize=(10, 8))
sns.heatmap(df_corr, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Mapa de Calor das Correlações')
plt.xticks(rotation=45)
plt.show()

# Gráfico de Barras
plt.figure(figsize=(10, 6))
df['Temporada_Cod'].value_counts().plot(kind='bar', color='skyblue', alpha=0.7)
plt.title('Quantidade de Produtos Vendidos por Temporada')
plt.xlabel('Temporada')
plt.ylabel('Vendas')
plt.xticks(rotation=45)
plt.show()

# Gráfico de Pizza
marca_counts = df['Marca_Freq'].value_counts() # Contagem de marcas

top5_marca = marca_counts.head(5) # Top 5 marcas

outros = marca_counts.iloc[5:].sum() # Soma das demais marcas
marcas_finais = pd.concat([top5_marca, pd.Series({'Outros': outros})]) # Agrupando as demais marcas em 'Outras'

plt.figure(figsize=(10, 6))
plt.pie(marcas_finais, labels=marcas_finais.index, autopct='%1.1f%%', startangle=140)
plt.title('Distribuição de Produtos por Marca')
plt.show()


# Gráfico de dispersão
plt.figure(figsize=(10, 6))
sns.kdeplot(df['Marca_Freq'], fill=True, color='blue')
plt.title('Distribuição de Frequência das Marcas')
plt.xlabel('Frequência')
plt.show()

# Gráfico de Regressão
sns.regplot(x='Marca_Cod', y='Marca_Freq', data=df, scatter_kws={'alpha':0.5, 'color':'red'})
plt.title('Gráfico de Regressão - Marca vs Frequência')
plt.xlabel('Marca')
plt.ylabel('Frequência')
plt.show()
