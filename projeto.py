import pandas as pd
from IPython.display import display
import plotly.express as px
df = pd.read_csv('projeto\projeto_dados_002\ClientesBanco.csv', encoding='latin1') # Carregando o dataframe, configurando para latin1
pd.set_option('display.max_columns', None) # Configurando para mostrar todas as colunas
df = df.drop('CLIENTNUM', axis=1) # Removendo a coluna CLIENTNUM, pois em primeira análise não é relevante
df = df.dropna() # Removendo linhas com valores ausentes
qnt_categoria = df['Categoria'].value_counts(normalize=True) # Calculando a quantidade percentual por categoria
#display(df.describe().round(1)) # Exibindo estatísticas descritivas arredondadas para 1 casa decimal
print("Quantidade percentual por categoria:")
display(qnt_categoria.round(2)) # Exibindo a quantidade percentual por categoria arredondada para 2 casas decimais
for coluna in df:
    fig = px.histogram(df, x=coluna, color='Categoria', barmode='group',
                   title=f'Distribuição de {coluna} por Categoria',)
    fig.show() # Exibindo histograma da idade segmentado por categoria
#Gráficos mostram que: 1° Quanto maior o número de contatos do cliente, maior a chance dele cancelar o cartão, 2° Clientes com mais produtos tendem a permanecer com o cartão, 3° Clientes que utilizam mais o cartão (maior gasto médio mensal) tendem a permanecer com o cartão.