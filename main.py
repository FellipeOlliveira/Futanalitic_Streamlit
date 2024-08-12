import pandas as pd
import streamlit as st
from engine import link_coletor
from utils.ligas import ligas_disponiveis
from utils import Time_casa, Time_fora

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
    links = link_coletor.coletar_partidas_time(ligas_disponiveis[liga_selecionada])
    if type(links)== list:
        links = pd.DataFrame(links,columns=[f'{liga_selecionada}'])
    st.subheader("Links das partidas analisadas")
    st.write(links)
    ##FIM COLETA LINKS

    #for i , partida in enumerate(links[liga_selecionada]):
    #st.subheader(f'Resultado Partida {i}:')
    #para testes :Sucesso
    time_casa = Time_casa.Casa(links[liga_selecionada])
    time_fora = Time_fora.Fora(links[liga_selecionada])
