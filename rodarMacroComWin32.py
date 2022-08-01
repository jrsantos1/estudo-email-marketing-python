import win32com.client as wincl
import os, os.path
import pandas as pd
#from IPython.display import display
from unittest import loader
from jinja2 import FileSystemLoader, Environment
from destinatarios import destinatarios


def lerExcel(tabela):
    dados = pd.read_excel(tabela)
    #display(dados)
    cont = 0
    dados_template = []
    for i, col in dados.iterrows():
        if col['MESA'] == 'SFF' and col['ALERTA'] > 0 and col['ALERTA'] < 3:
            dados_template.append([col['MESA'], col['ALERTA'], col['FUNDO'], col['VAR']])
            cont = cont + 1
    if cont > 1:
        print("Cheguei aqui")
        template = carregarTemplate(dados_template)
        enviarEmail(destinatarios['SFF'], template)

def rodarMacro():

    excel_macro = wincl.DispatchEx("Excel.application")
    excel_path = os.path.expanduser("C:\Git-Projects\\automates\\teste envio de email\\rodarMacro.xlsm")
    workbook = excel_macro.Workbooks.Open(Filename = excel_path) # ReadOnly =1
    excel_macro.Application.Run("rodarMacro.xlsm!Módulo1.rodarMacro")
    #Save the results in case you have generated data
    workbook.Save()
    excel_macro.Application.Quit()
    del excel_macro


def carregarTemplate(dados_template):
    loader = FileSystemLoader('templates')
    env = Environment(loader=loader)
    template = env.get_template('index2.html')

    file = open('output/index.html', 'w')

    render = template.render(dados = dados_template)
    file.write(render)
    file.close()
    return render

def enviarEmail(destinatario, template):

    outlook = wincl.Dispatch('outlook.application')

    # criando e-mail a partir da ingregracao com outlook
    email = outlook.CreateItem(0)

    # configurando informacoes do email
    # Para quem vai o e-mail // Assunto da mensagem

    email.To = destinatario + "; jrds.contato@hotmail.com; jrds.contato@gmail.com"
    email.Subject = 'e-mail automático de teste do python'

    # Criando e adicionando anexo
    # anexo = "C:\Git-Projects\\automates\\teste envio de email\email.xlsx"
    # email.Attachments.Add(anexo)

    email.HTMLBody = template

    email.Send()

lerExcel("rodarMacro.xlsm")