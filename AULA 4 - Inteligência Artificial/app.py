




# NOTAS DE ESTUDOS 


import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression


st.header('ANALISE DE NOTAS - PREVENDO')


estudos = pd.DataFrame({
'notas':[10,9,10,9.3,8,10,10],  # y
'horas':[2,4,5,7,9,10,5]        # x 
})


#st.scatter_chart(estudos, x = 'horas', y= 'notas')
modelo_escola = LinearRegression() 
modelo_escola.fit(estudos[['horas']], estudos['notas'])


h_estudo = st.number_input('horas de estudo')
# h_estudo = st.slider('horas de estudos', 0,30,5) # x 
nota_final = modelo_escola.predict([[h_estudo]])  # f(x)
print(nota_final)# y 


st.metric(f'sua nota seria' ,f'{min(nota_final[0], 10.0):.1f}') # y 