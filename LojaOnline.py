import streamlit as st
import pandas as pd
import csv
import PIL as image
import smtplib
import streamlit as st
import pandas as pd
import numpy as np

from collections import Counter
import streamlit as st
import pandas as pd
import numpy as np
import base64
from collections import Counter
import streamlit.components.v1 as components
import pandas as pd
import streamlit as st
import smtplib
import numpy as np

st.title(" A Loja online da Luna -  Livraria e DVDs e Séries")
Produtos=("Pipi das Meias Altas", " Filmes de Natal", " O Mundo de Patty", " Livros de Aventura", " Livros de Ciencia", "Encomendar")
Menu = st.multiselect("Escolha uma categoria de Produtos", Produtos)

Pesquisa = st.sidebar.text_input("Pesquisa por Livro/DVD")
button = st.sidebar.button("Pesquise Por TItulo", )

def send_mail(email, subject, message):
    try:
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.ehlo()
        server.starttls()
        username = 'maillefaun@gmail.com'
        password = 'qftabgvjolpfjniw'
        server.login(username, password)
        to_email = 'maillefaun@gmail.com'
        server.sendmail(username, to_email, mensagem)
        
        server.close()
    except Exception as e:
        st.error(f' Ocorreu um Erro ao enviar o e-mail, Desculpe: {e}')

with st.sidebar:

    
        
    email_form = st.form(key='my_email_form', clear_on_submit=False)
    email = email_form.text_input(label='Por Favor Escreva o Seu Endereço de e-mail')
    
    subject = email_form.text_input (label = ' Escreva aqui o Assunto ' )
    message = email_form.text_area (label = ' Escreva a sua Mensagem ')
        
    if email_form.form_submit_button(label=' Enviar '):
        mensagem = f'Subject:{subject}\n\n De: {email}\n\n Assunto: {message}'.encode('utf-8')
        send_mail(email, subject, message)
        st.subheader('  Mensagem enviada com Sucesso!') 
    
    option_menu = ["Home", "Encomendar"]
    
    Menu = st.multiselect("Escolha uma categoria de Produtos", option_menu)
    
if Menu == 'Encomendar':
    
    email_form = st.form(key='my_email_form', clear_on_submit=False)
    email = email_form.text_input(label='Por Favor Escreva o Seu Endereço de e-mail')
    
    subject = email_form.text_input (label = ' Escreva aqui o Assunto ' )
    message = email_form.text_area (label = ' Escreva a sua Mensagem ')
        
    if email_form.form_submit_button(label=' Enviar '):
        mensagem = f'Subject:{subject}\n\n De: {email}\n\n Assunto: {message}'.encode('utf-8')
        send_mail(email, subject, message)
        st.subheader('  Mensagem enviada com Sucesso!') 


    col1, col2, col3 = st.columns(3)
    
with col1:
    st.header(" Coleção DVD1")
    st.image("12AF4C15-C421-478E-944C-8F42B9B50185.png")
    Button1 = st.number_input("Quantidade e adicione ao Carrinho", key="Core")
with col2:
    st.header("DVD 2 PIPI")
    st.image("07944EEF-7714-493A-94A0-D512BA71DF47.png")
    Button2 = st.number_input("Quantidade e adicione ao Carrinho", key="Alba")
with col3:
    st.header("A Lassie")
    st.image("IMG_5123.png")
    Button3=st.number_input("Quantidade e adicione ao Carrinho", key="Delta")
if Menu == 'O Mundo de Patty':
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("IMG_5131.png")
        Button4=st.number_input("Quantidade e adicione ao Carrinho", key="Coresey")
    with col2:
        st.image("IMG_5124.png")
        Button5=st.number_input("Quantidade e adicione ao Carrinho", key="Ypsilon")
    with col3:
        st.image("IMG_5130.png")
        Button6=st.number_input("Quantidade e adicione ao Carrinho", key="image")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("IMG_5131.png")
        Button7=st.number_input("Quantidade e adicione ao Carrinho", key="Cosey")
    with col2:
        st.image("IMG_5124.png")
        Button8=st.number_input("Quantidade e adicione ao Carrinho", key="Yplon")
    with col3:
        st.image("IMG_5130.png")
        Button9=st.number_input("Quantidade e adicione ao Carrinho", key="lta")
