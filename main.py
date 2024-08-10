import streamlit as st
from engine import teste
from bs4 import BeautifulSoup
from utils.ligas import ligas_disponiveis

# Criação do menu lateral
st.sidebar.header("Menu de Análise")

#select option
opcao = st.sidebar.selectbox("Escolha uma liga:", [liga for liga in ligas_disponiveis.keys()])


# Conteúdo principal da página
st.title("Futanalitic")
st.write("Utilize o menu lateral para inserir os dados e realizar a análise.")

# Botão de Analisar
if st.sidebar.button("Analisar"):
    result = teste.requisicao_test()
    st.write(f"Resultado do Teste : {result}")
