import streamlit as st
import pandas as pd
import csv
import PIL as image

import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
from collections import Counter

st.title(" A Loja online da Luna -  Livraria e DVDs e Séries")
Produtos=("Pipi das Meias Altas", " Filmes de Natal", " O Mundo de Patty", " Livros de Aventura", " Livros de Ciencia")
Menu = st.multiselect("Escolha uma categoria de Produtos", Produtos)

Pesquisa = st.sidebar.text_input("Pesquisa por Livro/DVD")
button = st.sidebar.button("Pesquise Por TItulo", )



with st.sidebar:

    email_form = st.form(key='my_email_form', clear_on_submit=False)
    email = email_form.text_input(label='Por Favor Escreva o Seu Endereço de e-mail')
    with st.expander("See explanation"):
        emailsubject = email_form.text_input(label=' Escreva aqui o Assunto ')
        emailmessage = email_form.text_area(label=' Escreva a sua Mensagem ')

        submit_e_button = email_form.form_submit_button(label='Enviar')

    if submit_e_button:
        st.subheader('  Mensagem enviada com Sucesso!')
    option_menu = ["Home", "Encomendar"]
    Menu = st.multiselect("Escolha uma categoria de Produtos", option_menu)
    if option_menu == 'Encomendar':
        email_form = st.form(key='my_email_form', clear_on_submit=False)
        email = email_form.text_input(label='Por Favor Escreva o Seu Endereço de e-mail')
        with st.expander("See explanation"):
            emailsubject = email_form.text_input (label = ' Escreva aqui o Assunto ')
            emailmessage = email_form.text_area (label = ' Escreva a sua Mensagem ')

            submit_e_button = email_form.form_submit_button(label='Enviar' )

        if submit_e_button == True:
            st.subheader('  Mensagem enviada com Sucesso!')

if option_menu == 'Encomendar':
    email_form = st.form(key='my_email_form', clear_on_submit=False)
    email = email_form.text_input(label='Por Favor Escreva o Seu Endereço de e-mail')
    with st.expander("See explanation"):
        emailsubject = email_form.text_input(label=' Escreva aqui o Assunto ')
        emailmessage = email_form.text_area(label=' Escreva a sua Mensagem ')

        submit_e_button = email_form.form_submit_button(label='Enviar')

    if submit_e_button:
        st.subheader('  Mensagem enviada com Sucesso!')

col1, col2, col3 = st.columns(3)

with col1:
    st.header(" Coleção DVD1")
    st.image("/Users/paulomonteiro/PycharmProjects/Formulário_Alunos/12AF4C15-C421-478E-944C-8F42B9B50185.png")
    Button1 = st.number_input("Quantidade e adicione ao Carrinho", key="Core")
with col2:
    st.header("DVD 2 PIPI")
    st.image("/Users/paulomonteiro/PycharmProjects/Formulário_Alunos/07944EEF-7714-493A-94A0-D512BA71DF47.png")
    Button2 = st.number_input("Quantidade e adicione ao Carrinho", key="Alba")
with col3:
    st.header("A Lassie")
    st.image("/Users/paulomonteiro/PycharmProjects/Formulário_Alunos/IMG_5123.png")
    Button3=st.number_input("Quantidade e adicione ao Carrinho", key="Delta")

col1, col2, col3 = st.columns(3)
with col1:
    st.image("/Users/paulomonteiro/PycharmProjects/Formulário_Alunos/IMG_5131.png")
    Button4=st.number_input("Quantidade e adicione ao Carrinho", key="Coresey")
with col2:
    st.image("/Users/paulomonteiro/PycharmProjects/Formulário_Alunos/IMG_5124.png")
    Button5=st.number_input("Quantidade e adicione ao Carrinho", key="Ypsilon")
with col3:
    st.image("/Users/paulomonteiro/PycharmProjects/Formulário_Alunos/IMG_5130.png")
    Button6=st.number_input("Quantidade e adicione ao Carrinho", key="image")

col1, col2, col3 = st.columns(3)
with col1:
    st.image("/Users/paulomonteiro/PycharmProjects/Formulário_Alunos/IMG_5131.png")
    Button7=st.number_input("Quantidade e adicione ao Carrinho", key="Cosey")
with col2:
    st.image("/Users/paulomonteiro/PycharmProjects/Formulário_Alunos/IMG_5124.png")
    Button8=st.number_input("Quantidade e adicione ao Carrinho", key="Yplon")
with col3:
    st.image("/Users/paulomonteiro/PycharmProjects/Formulário_Alunos/IMG_5130.png")
    Button9=st.number_input("Quantidade e adicione ao Carrinho", key="lta")
