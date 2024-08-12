import pandas as pd
import streamlit as st
from engine import link_coletor
from utils.ligas import ligas_disponiveis
from time import sleep
import pandas

# Criação do menu lateral
st.sidebar.header("Menu de Análise")

#select option
liga_selecionada = st.sidebar.selectbox("Escolha uma liga:", [liga for liga in ligas_disponiveis.keys()],key='selectbox_liga')

# Conteúdo principal da página
st.title("Futanalitic")
st.write("Utilize o menu lateral para inserir os dados e realizar a análise.")

# Botão de Analisar
if st.sidebar.button("Analisar",key='btn_analisar'):
    result = link_coletor.coletar_partidas_time(ligas_disponiveis[liga_selecionada])
    if type(result)== list:
        result = pd.DataFrame(result,columns=[f'Link partidas: {liga_selecionada}'])
    st.subheader("Links das partidas analisadas")
    st.write(result)
    ##FIM COLETA LINKS

    st.write("macaco")
