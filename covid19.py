import pandas as pd
import plotly.express as px
import streamlit as st

#streamlit run codigoBase.py

df = pd.read.csv("https://raw.githubusercontent.com/wcota/covid19br/master/cases-brazil-states.csv")

df = df.rename(columns = {'newDeaths' : 'Novos Óbitos', 'newCases' : 'Novos Casos', 'deaths_per_100k_inhabitants' : 'Óbitos por 100 mil habitantes', 'totalCases_per_100k_inhabitants' : 'Casos por 100 mil habitantes'})

estados = list(df['state'].unique())
state = st.sidebar.selectbox('Selecione o estado', estados)

colunas = ['Novos Óbitos','Novos Casos','Óbitos por 100 mil habitantes', 'Casos por 100 mil habitantes']
column = st.sidebar.selectbox('Qual tipo de informação ?', colunas)

df = df[df['state'] == state] #seleção de linhas que pertencem ao estado

fig = px.line(df, x="date", y=column, title=column + ' - ' + state)
fig.update_layout(xaxis_title='Data', yaxis_title=column.upper(), title = {'x':0.5})

st.title('DADOS COVID19 BRASIL')
st.write('Nessa aplicação, você terá a opção de escolher o estado e o tipo de informação para mostrar o gráfico, utilize o menu lateral para alterar os dados')

st.plotly_chart(fig, use_container_width=True)

st.caption('Os dados foram obtidos a partir do site https://github.com/wcota/covid19br')

