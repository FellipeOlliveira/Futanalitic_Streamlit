import streamlit as st
import src
# Criação do menu lateral
st.sidebar.header("Menu de Análise")

# Select option
opcao = st.sidebar.selectbox("Escolha uma opção:", ["Opção 1", "Opção 2", "Opção 3"])


# Conteúdo principal da página
st.title("Futanalitic")
st.write("Utilize o menu lateral para inserir os dados e realizar a análise.")

# Botão de Analisar
if st.sidebar.button("Analisar"):
    result = src.teste.requisicao_test()
    st.write(f"Resultado do Teste : {result}")