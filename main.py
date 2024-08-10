import streamlit as st
from engine import coletor
from utils.ligas import ligas_disponiveis

# Criação do menu lateral
st.sidebar.header("Menu de Análise")

#select option
liga_selecionada = st.sidebar.selectbox("Escolha uma liga:", [liga for liga in ligas_disponiveis.keys()])


# Conteúdo principal da página
st.title("Futanalitic")
st.write("Utilize o menu lateral para inserir os dados e realizar a análise.")

# Botão de Analisar
if st.sidebar.button("Analisar"):
    result = coletor.coletar_partidas_time(ligas_disponiveis[liga_selecionada])
    st.write(result)
