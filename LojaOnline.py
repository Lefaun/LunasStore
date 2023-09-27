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

import pandas as pd

class ListarNome():
    def __init__(self):
        self.Livros = []
        self.Lista = []

    def add_Nome(self, livro, preco):
        self.Lista.append(livro)
        self.Lista.append(preco)
        Lista_de_Livros = self.Lista
        with open('Lista_de_Livros - Folha1.csv', 'w', newline='') as file:
            writer = csv.writer(file, delimiter=',')
            Lista_de_Livros = writer.writerow(self.Lista) 
            df = pd.to_csv(Lista_de_Livros)

            st.write(df)

        
        
        
        #with open('Lista_de_Livros - Folha1.csv', 'w', newline='') as file:
           
            #writer = csv.writer(file, delimiter=',')
            #self.Livros = writer.writerow(livro) 
            #data = writer.writerows(livro)
            
            #df = pd.DataFrame(Livros)
            
            
            
            #st.write(df)
        
        if st.success:
        
            st.write("Livro adicionado com Sucesso")
            
        else:
            st.write("Esse valor para Livro não é Válido")
                    
           
            
    def tirar_Nome(self, livro):
        if livro in self.Livros:
            self.Livros.remove(livro)
            st.write(f"O {Livro} foi removido da lista com sucesso.")
        else:
            st.write("O Livro introduzido não é válido.")

    def Listar_Nome(self):
        st.write("Os nomes que constam da lista são:")
        #for livro in self.Livros:
        
        with open('Lista_de_Livros - Folha1.csv', 'r') as file:
            reader = csv.reader(file)
            df = pd.DataFrame(reader)
            st.write(df)
            #for row in reader:
                #st.write(row)
            
    def Consultar(self):
        item_procurado= st.text_input("Consulte um Livro")
        df = pd.read_csv('Lista_de_Livros - Folha1.csv')
        st.write(df, width= 800)
        #Livros_a_Verificar = pd.read_csv('Lista_de_Livros - Folha1.csv')
        #filter =  [Search in Livros_a_Verificar for livro in df['Livros']]
        # create a sample DataFrame
        #df = pd.DataFrame({'fruit': ['apple', 'banana', 'pear', 'kiwi', 'orange']})
        
        # create a list of fruits we are interested in
        df = pd.DataFrame({'Livros': ['Coleção DVD1', 'A Lassie', 'Filmes de Natal', 'Floribella RI-Fixe', 'Mundo de Patty 1', 'Mundo de Patty ', 'Mundo de Patty 3']})
        Livros_a_Verificar = ['Coleção DVD1', 'A Lassie', 'Filmes de Natal', 'Floribella RI-Fixe', 'Mundo de Patty 1', 'Mundo de Patty ', 'Mundo de Patty 3','O Mundo de Patty', 'Filme de Natal']
        
        
        # print the resulting DataFrame, containing only the rows that match the mask
        filter = [item_procurado in Livros_a_Verificar for items in df['Livros']]
            # Encontre a linha onde o item corresponde
           
            #linha_item = df[df['Livros'] == item_procurado]
        
            # Extraia a descrição, preço e imagem correspondentes
            #descricao = linha_item['Descrição'].values[0]
            #preco = linha_item['Preço'].values[0]
            #imagem = linha_item['Imagem'].values[0]
        
            # Exiba os resultados
            #print(f"Item: {item_procurado}")
            #print(f"Descrição: {descricao}")
            #print(f"Preço: {preco}")
            #print(f"Imagem: {imagem}")
        
        if item_procurado in filter:   
            st.write(f"este {item_procurado} encontra-se na Lista")
            st.write(df[filter])
        else:
            st.write(f"este {item_procurado} não encontra-se na Lista")
            st.write(df[filter])
       
        #with open('Lista_de_Livros - Folha1.csv', 'r') as file:
            #reader = csv.reader(file)
            #df = pd.DataFrame(reader)
            #if Search in reader['Livros'].values:
                #linha_item = reader[reader['Livros']==Search]

                #descricao =  linha_item['Descricao'].values[0]
                #preco =  linha_item['preco'].values[0]
                #st.write(f" Item: {item_procurado}")
        

        
        #não deu para criar um   create a sample DataFrame
        #df = pd.DataFrame({'Livros': ['Coleção DVD1', 'A Lassie', 'Filmes de Natal', 'Floribella RI-Fixe', 'Mundo de Patty 1', 'Mundo de Patty ', 'Mundo de Patty 3']})
        # create a list of fruits we are interested in
        #Livros_a_Verificar = ['Coleção DVD1', 'A Lassie', 'Filmes de Natal', 'Floribella RI-Fixe', 'Mundo de Patty 1', 'Mundo de Patty ', 'Mundo de Patty 3','O Mundo de Patty', 'Filme de Natal']
        
        # check if the 'fruit' column contains any of the fruits we are interested in
        #filter =  [Search in Livros_a_Verificar for livro in df['Livros']]
        #livro in Livros_a_Verificar for 
        # print the resulting DataFrame, containing only the rows that match the mask
        
        #for row in reader:
        
    def Menu_Completo(self):
        
        Encomendas = ["1. Adicionar à Lista", "2. Remover da Lista", "3. Consultar Lista", "4. Consultar um Livro", "5. Sair do Programa" ]
        #opcao = st.text_input("Escolha uma opção - por favor:")
        opcao = st.selectbox("Selecione uma Opção", Encomendas)
        
        if opcao == "1. Adicionar à Lista":
            livro  = st.text_input("Qual o Livro que pretende encomendar: ")
            preco  = st.text_input("Qual Preço do Livro a encomendar: ")
            self.add_Nome(self,livro)
        elif opcao == "2. Remover da Lista":
            nome = st.text_input("Qual o Livro que pretende remover: ")
            self.tirar_Nome(livro)
        elif opcao == "3. Consultar Lista":
            self.Listar_Nome()
        elif opcao == "4. Consultar um Livro":
            self.Consultar()
        elif opcao == "5. Sair do Programa":
            st.write("Sair")
            

        #df = pd.DataFrame(self.Livros)
        
        




st.title(" A Loja online da Luna -  Livraria e DVDs e Séries")
st.write("adiciona ao teu carrinho ou segue pela opção Encomendar no menu lateral ou nas opções da página")

Menu=("Encomendar","Pipi das Meias Altas", " Filmes de Natal", " O Mundo de Patty", " Livros de Aventura", " Livros de Ciencia", )
components.html(
    """<!-- Hotjar Tracking Code for https://lunastore.streamlit.app/ -->
<script>
    (function(h,o,t,j,a,r){
        h.hj=h.hj||function(){(h.hj.q=h.hj.q||[]).push(arguments)};
        h._hjSettings={hjid:3661255,hjsv:6};
        a=o.getElementsByTagName('head')[0];
        r=o.createElement('script');r.async=1;
        r.src=t+h._hjSettings.hjid+j+h._hjSettings.hjsv;
        a.appendChild(r);
    })(window,document,'https://static.hotjar.com/c/hotjar-','.js?sv=');
</script>""")

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
        server.sendmail(username, to_email, mensagem,  )
        
        server.close()
    except Exception as e:
        st.error(f' Ocorreu um Erro ao enviar o e-mail, Desculpe: {e}')

class EmailSend():
    def __init__(self, mail, send_mail):
        self.mail = mail
        self.send_mail = send_mail
    
    def send_mail(email, subject, message):
        try:
            server = smtplib.SMTP('smtp.gmail.com',587)
            server.ehlo()
            server.starttls()
            username = 'maillefaun@gmail.com'
            password = 'qftabgvjolpfjniw'
            server.login(username, password)
            to_email = 'maillefaun@gmail.com'
            server.sendmail(username, to_email, mensagem,  )
            
            server.close()
        except Exception as e:
            st.error(f' Ocorreu um Erro ao enviar o e-mail, Desculpe: {e}')
        
    def mail(email_form, email, subject, message, encomenda,):
            
        email_form = st.form(key='my_email_form4', clear_on_submit=False)
        email = email_form.text_input(label='Por Favor Escreva o Seu Endereço de e-mail')
    
        subject = email_form.text_input (label = ' Escreva aqui o Assunto ' )
        message = email_form.text_area (label = ' Escreva a sua Mensagem ')
        encomenda = email_form.text_area (label = ' Artigos e Quantidade ', value = Encomendas )
    
        if email_form.form_submit_button(label='Enviar'):
            mensagem = f'Subject:{subject}\n\n De: {email}\n\n Assunto: {message}, Artigos: {encomenda}'.encode('utf-8')
            send_mail(email, subject, message, )
            st.subheader('  Mensagem enviada com Sucesso!') 
            st.write(Encomendas)

with st.sidebar:

    st.image("AI_Monster_Book_eater.png" , width=300)
    
    
    

    
    email_form = st.form(key='my_email_form', clear_on_submit=False)
    email = email_form.text_input(label='Por Favor Escreva o Seu Endereço de e-mail')
    
    subject = email_form.text_input (label = ' Escreva aqui o Assunto ' )
    message = email_form.text_area (label = ' Escreva a sua Mensagem ')
    encomenda = email_form.text_area (label = ' Artigos e Quantidade ' , value = Encomendas)
    
    if email_form.form_submit_button(label=' Enviar '):
        mensagem = f'Subject:{subject}\n\n De: {email}\n\n Assunto: {message}, Artigos: {encomenda}'.encode('utf-8')
        send_mail(email, subject, message)
        st.subheader('  Mensagem enviada com Sucesso!')
    
    
if choice == 'Encomendar':
    lista_nomes = ListarNome()
    lista_nomes.Menu_Completo()
    
    email_form = st.form(key='my_email_form2', clear_on_submit=False)
    email = email_form.text_input(label='Por Favor Escreva o Seu Endereço de e-mail')
    
    subject = email_form.text_input (label = ' Escreva aqui o Assunto ' )
    message = email_form.text_area (label = ' Escreva a sua Mensagem ')
    encomenda = email_form.text_area (label = ' Artigos e Quantidade ', value = Encomendas )
    
    if email_form.form_submit_button(label='Enviar'):
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
        REF1 = str("Encomenda PIPI 1: 3€")
        if Button1 >0:
            Encomendas.append(REF1)
    with col2:
        st.header("DVD 2 PIPI")
        st.image("07944EEF-7714-493A-94A0-D512BA71DF47.png")
        Button2 = st.number_input("Quantidade e adicione ao Carrinho",min_value=0, key="Alba")
        REF2 = str("Encomenda PIPI 2: 3€")
        if Button2 >0:
            Encomendas.append(REF2)
    with col3:
        st.header("A Lassie")
        st.image("IMG_5123.png")
        Button3=st.number_input("Quantidade e adicione ao Carrinho",min_value=0, key="Delta")
        REF3 = str("Encomenda Lassie: 3€")
        if Button3 >0:
            Encomendas.append(REF3)
    col1, col2 =st.columns(2)
    with col1:
        st.header(Encomendas)
    with col2:
        Confirmar = st.button("Confirmar")
        
        email_form = st.form(key='my_email_form2', clear_on_submit=False)
        email = email_form.text_input(label='Por Favor Escreva o Seu Endereço de e-mail')
        
        subject = email_form.text_input (label = ' Escreva aqui o Assunto ' )
        message = email_form.text_area (label = ' Escreva a sua Mensagem ')
        encomenda = email_form.text_area (label = ' Artigos e Quantidade ', value = Encomendas )

        if email_form.form_submit_button(label='Enviar'):
            mensagem = f'Subject:{subject}\n\n De: {email}\n\n Assunto: {message}, Artigos: {encomenda}'.encode('utf-8')
            send_mail(email, subject, message, )
            st.subheader('  Mensagem enviada com Sucesso!') 
            st.write(Encomendas)

if choice == ' O Mundo de Patty':
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("Mundo de Patty1.jpeg")
        Button4=st.number_input("Quantidade e adicione ao Carrinho",min_value=0, key="Coresey")
        REF4 = str("Mundo de Patty 1 - Unidade 3€")
        if Button4 >0:
            Encomendas.append(REF4)
    with col2:
        st.image("Mundo de Patty2.jpeg")
        Button5=st.number_input("Quantidade e adicione ao Carrinho",min_value=0, key="Ypsilon2")
        REF5 = str("Mundo Patty2 - Coleção 5 DVD : 5€")
        if Button5 >0:
            Encomendas.append(REF5)
    with col3:
        st.image("Mundo de Patty3.jpeg")
        Button6=st.number_input("Quantidade e adicione ao Carrinho",min_value=0, key="image2")
        REF6 = str("Mundo Patty3- Unidade 3€")
        if Button6 >0:
            Encomendas.append(REF6)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("Mundo de Patty4.jpeg")
        Button10=st.number_input("Quantidade e adicione ao Carrinho",min_value=0, key="Coresey2")
        REF10 = str("Mundo de Patty4C-oleção 5 DVD : 5€")
        if Button4 >0:
            Encomendas.append(REF10)
    with col2:
        st.image("Mundo de Patty5.jpeg")
        Button11=st.number_input("Quantidade e adicione ao Carrinho",min_value=0, key="Ypsilon")
        REF11 = str("Mundo Patty5- Unidade 3€")
        if Button11 >0:
            Encomendas.append(REF11)
    with col3:
        st.image("Mundo de Patty6.jpeg")
        Button12=st.number_input("Quantidade e adicione ao Carrinho",min_value=0, key="image")
        REF12 = str("Mundo Patty6- Unidade 3€")
        if Button12 >0:
            Encomendas.append(REF12)
    
    st.header(Encomendas)
    st.write(df)
    Confirmar = st.button("Confirmar")
    
    email_form = st.form(key='my_email_form2', clear_on_submit=False)
    email = email_form.text_input(label='Por Favor Escreva o Seu Endereço de e-mail')
    
    subject = email_form.text_input (label = ' Escreva aqui o Assunto ' )
    message = email_form.text_area (label = ' Escreva a sua Mensagem ')
    encomenda = email_form.text_area (label = ' Artigos e Quantidade ', value = Encomendas )

    if email_form.form_submit_button(label='Enviar'):
        mensagem = f'Subject:{subject}\n\n De: {email}\n\n Assunto: {message}, Artigos: {encomenda}'.encode('utf-8')
        send_mail(email, subject, message, )
        st.subheader('  Mensagem enviada com Sucesso!') 
        st.write(Encomendas)

            
if choice == " Filmes de Natal":
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("IMG_5131.png")
        Button7=st.number_input("Quantidade e adicione ao Carrinho",min_value=0, key="Cosey")
        REF7 = str("Floribela MEGA RI Fixe")
        if Button7 >0:
            Encomendas.append(REF7)
    with col2:
        st.image("IMG_5124.png")
        Button8=st.number_input("Quantidade e adicione ao Carrinho",min_value=0, key="Yplon")
        REF8 = str("filme de Natal: 3€")
        if Button8 >0:
            Encomendas.append(REF8)
    with col3:
        st.image("IMG_5130.png")
        Button9=st.number_input("Quantidade e adicione ao Carrinho",min_value=0, key="lta")
        REF9 = str("Mundo de Barbie na Moda: 3€")
        if Button9 >0:
            Encomendas.append(REF9)
    col1, col2 =st.columns(2)
    with col1:
        st.header(Encomendas)
    with col2: 
        Confirmar = st.button("Confirmar")
        email_form = st.form(key='my_email_form3', clear_on_submit=False)
        email = email_form.text_input(label='Por Favor Escreva o Seu Endereço de e-mail')
        
        subject = email_form.text_input (label = ' Escreva aqui o Assunto ' )
        message = email_form.text_area (label = ' Escreva a sua Mensagem ')
        encomenda = email_form.text_area (label = ' Artigos e Quantidade ', value = Encomendas )
    
        if email_form.form_submit_button(label='Enviar'):
            mensagem = f'Subject:{subject}\n\n De: {email}\n\n Assunto: {message}, Artigos: {encomenda}'.encode('utf-8')
            send_mail(email, subject, message, )
            st.subheader('  Mensagem enviada com Sucesso!') 
            st.write(Encomendas)
    
if choice == " Livros de Ciencia":
    col1, col2, col3 = st.columns(3)
        
    with col1:
        st.header(" Revista National Geographic")
        st.image("Revista_NG_Cerebro.jpeg")
        Button20 = st.number_input("Quantidade e adicione ao Carrinho",min_value=0, key="Core2")
        REF20 = str("Revista National Geographic Cérebro- 15€")
        if Button20 >0:
            Encomendas.append(REF20)
    with col2:
        st.header("Revista Monocle")
        st.image("Monocle.jpeg")
        Button21 = st.number_input("Quantidade e adicione ao Carrinho",min_value=0, key="Alba2")
        REF21 = str("Revista Cultura e artes - Monocle - unidade 13€")
        if Button21 >0:
            Encomendas.append(REF21)
    with col3:
        st.header("Coleção Revistas VIsão e Sábado")
        st.image("Coleção5Revistas Visao.jpeg")
        Button23=st.number_input("Quantidade e adicione ao Carrinho",min_value=0, key="Delta2")
        REF23 = str("10 Revistas - 15€")
        if Button23 >0:
            Encomendas.append(REF23)
    
    col1, col2, col3 = st.columns(3)
        
    with col1:
        st.header(" Livro De Psicologia")
        st.image("Psicologia.jpeg")
        Button30 = st.number_input("Quantidade e adicione ao Carrinho",min_value=0, key="Core21")
        REF30 = str("Livro De Psicologia- 12€")
        if Button30 >0:
            Encomendas.append(REF30)
    with col2:
        st.header("Livro - Nação Dopamina")
        st.image("dopamina.jpeg")
        Button31 = st.number_input("Quantidade e adicione ao Carrinho",min_value=0, key="Alba21")
        REF31 = str("Livro - Nação Dopamina 15€")
        if Button31 >0:
            Encomendas.append(REF31)
    with col3:
        st.header("Coleção de Livros")
        
    
    st.header(Encomendas)

    Confirmar = st.button("Confirmar")
    
    email_form = st.form(key='my_email_for7', clear_on_submit=False)
    email = email_form.text_input(label='Por Favor Escreva o Seu Endereço de e-mail')
    
    subject = email_form.text_input (label = ' Escreva aqui o Assunto ' )
    message = email_form.text_area (label = ' Escreva a sua Mensagem ')
    encomenda = email_form.text_area (label = ' Artigos e Quantidade ', value = Encomendas )

    if email_form.form_submit_button(label='Enviar'):
        mensagem = f'Subject:{subject}\n\n De: {email}\n\n Assunto: {message}, Artigos: {encomenda}'.encode('utf-8')
        send_mail(email, subject, message, )
        st.subheader('  Mensagem enviada com Sucesso!') 
        st.write(Encomendas)
        
        #email_form = st.form(key='my_email_form5', clear_on_submit=False)
        #email = email_form.text_input(label='Por Favor Escreva o Seu Endereço de e-mail')
        
        #subject = email_form.text_input (label = ' Escreva aqui o Assunto ' )
        #message = email_form.text_area (label = ' Escreva a sua Mensagem ')
        #encomenda = email_form.text_area (label = ' Artigos e Quantidade ' , value = Encomendas)
        
    
    #if email_form.form_submit_button(label=' Submeter Pedido '):
    #    mensagem = f'Subject:{subject}\n\n De: {email}\n\n Assunto: {message}, Artigos: {encomenda}'.encode('utf-8')
    #    send_mail(email, subject, message)
    #    st.subheader('  Mensagem enviada com Sucesso!')

        

