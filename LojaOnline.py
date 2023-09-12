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
Menu=("Pipi das Meias Altas", " Filmes de Natal", " O Mundo de Patty", " Livros de Aventura", " Livros de Ciencia", "Encomendar")

choice = st.selectbox("Selecione uma Opção", Menu)
Encomendas = []
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
        server.sendmail(username, to_email, mensagem, )
        
        server.close()
    except Exception as e:
        st.error(f' Ocorreu um Erro ao enviar o e-mail, Desculpe: {e}')

with st.sidebar:

    
        
    email_form = st.form(key='my_email_form', clear_on_submit=False)
    email = email_form.text_input(label='Por Favor Escreva o Seu Endereço de e-mail')
    
    subject = email_form.text_input (label = ' Escreva aqui o Assunto ' )
    message = email_form.text_area (label = ' Escreva a sua Mensagem ')
    encomenda = email_form.text_area (label = ' Artigos e Quantidade ' , value = Encomendas)
    
    if email_form.form_submit_button(label=' Enviar '):
        mensagem = f'Subject:{subject}\n\n De: {email}\n\n Assunto: {message}, Artigos: {encomenda}'.encode('utf-8')
        send_mail(email, subject, message, )
        st.subheader('  Mensagem enviada com Sucesso!')
    
    
if choice == 'Encomendar':
    
    email_form = st.form(key='my_email_form2', clear_on_submit=False)
    email = email_form.text_input(label='Por Favor Escreva o Seu Endereço de e-mail')
    
    subject = email_form.text_input (label = ' Escreva aqui o Assunto ' )
    message = email_form.text_area (label = ' Escreva a sua Mensagem ')
    encomenda = email_form.text_area (label = ' Artigos e Quantidade ', value = Encomendas )
    
    if email_form.form_submit_button(label=' Enviar '):
        mensagem = f'Subject:{subject}\n\n De: {email}\n\n Assunto: {message}, Artigos: {encomenda}'.encode('utf-8')
        send_mail(email, subject, message, )
        st.subheader('  Mensagem enviada com Sucesso!') 
        st.write(Encomendas)
if choice == 'Pipi das Meias Altas':
    col1, col2, col3 = st.columns(3)
        
    with col1:
        st.header(" Coleção DVD1")
        st.image("12AF4C15-C421-478E-944C-8F42B9B50185.png")
        Button1 = st.number_input("Quantidade e adicione ao Carrinho",min_value=0, key="Core")
        REF1 = str("Encomenda PIPI 1")
        if Button1 >0:
            Encomendas.append(REF1)
    with col2:
        st.header("DVD 2 PIPI")
        st.image("07944EEF-7714-493A-94A0-D512BA71DF47.png")
        Button2 = st.number_input("Quantidade e adicione ao Carrinho",min_value=0, key="Alba")
        REF2 = str("Encomenda PIPI 2")
        if Button2 >0:
            Encomendas.append(REF2)
    with col3:
        st.header("A Lassie")
        st.image("IMG_5123.png")
        Button3=st.number_input("Quantidade e adicione ao Carrinho",min_value=0, key="Delta")
        REF3 = str("Encomenda Lassie")
        if Button3 >0:
            Encomendas.append(REF3)
    col1, col2 =st.columns(2)
    with col1:
        st.header(Encomendas)
    with col2:
        Confirmar = st.button("Confirmar")

if Confirmar == True:
    email_form = st.form(key='my_email_form3', clear_on_submit=False)
    email = email_form.text_input(label='Por Favor Escreva o Seu Endereço de e-mail')
    
    subject = email_form.text_input (label = ' Escreva aqui o Assunto ' )
    message = email_form.text_area (label = ' Escreva a sua Mensagem ')
    encomenda = email_form.text_area (label = ' Artigos e Quantidade ' , value = Encomendas)
    
    if email_form.form_submit_button(label=' Enviar '):
        mensagem = f'Subject:{subject}\n\n De: {email}\n\n Assunto: {message}, Artigos: {encomenda}'.encode('utf-8')
        send_mail(email, subject, message, )
        st.subheader('  Mensagem enviada com Sucesso!')

if choice == ' O Mundo de Patty':
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("IMG_5131.png")
        Button4=st.number_input("Quantidade e adicione ao Carrinho",min_value=0, key="Coresey")
    with col2:
        st.image("IMG_5124.png")
        Button5=st.number_input("Quantidade e adicione ao Carrinho",min_value=0, key="Ypsilon")
    with col3:
        st.image("IMG_5130.png")
        Button6=st.number_input("Quantidade e adicione ao Carrinho",min_value=0, key="image")
if choice == " Filmes de Natal":
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("IMG_5131.png")
        Button7=st.number_input("Quantidade e adicione ao Carrinho",min_value=0, key="Cosey")
    with col2:
        st.image("IMG_5124.png")
        Button8=st.number_input("Quantidade e adicione ao Carrinho",min_value=0, key="Yplon")
    with col3:
        st.image("IMG_5130.png")
        Button9=st.number_input("Quantidade e adicione ao Carrinho",min_value=0, key="lta")
