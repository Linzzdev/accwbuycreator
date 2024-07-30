import time
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from PyPDF2 import PdfReader
import re
import sys

# EXTRAIR PDF
def extrair_informacoes(texto):
    informacoes = {}

    nome_loja = r'Nome da sua Loja:\s*(.*)'
    nome = r'Nome:\s*(.*)'
    telefone = r'Telefone:\s*(.*)'
    cidade = r'Cidade:\s*(.*)'
    estado = r'Estado:\s*(.*)'
    plano = r'Plano:\s*(.*)'
    email = r'Email:\s*(.*)'

    informacoes['nome_loja'] = re.search(nome_loja, texto).group(1).strip() if re.search(nome_loja, texto) else None
    informacoes['nome'] = re.search(nome, texto).group(1).strip() if re.search(nome, texto) else None
    informacoes['telefone'] = re.search(telefone, texto).group(1).strip() if re.search(telefone, texto) else None
    informacoes['cidade'] = re.search(cidade, texto).group(1).strip() if re.search(cidade, texto) else None
    informacoes['estado'] = re.search(estado, texto).group(1).strip() if re.search(estado, texto) else None
    informacoes['plano'] = re.search(plano, texto).group(1).strip() if re.search(plano, texto) else None
    informacoes['email'] = re.search(email, texto).group(1).strip() if re.search(email, texto) else None
    
    return informacoes

def cadastrowBuy():
    try:
        edge_options = EdgeOptions()
        edge_service = EdgeService(executable_path=edge_driver_path)
        driver = webdriver.Edge(service=edge_service, options=edge_options)
        driver.get("https://www.wbuy.com.br/criar-loja-virtual/")
        time.sleep(2)
    
    # Campo Nome da sua Loja
        search_box_nomeLoja = driver.find_element(By.XPATH, '//*[@id="frmCriarLoja"]/div/div/div[1]/div/input')
        search_box_nomeLoja.send_keys(informacoes['nome_loja'])
        time.sleep(1)
        if search_box_nomeLoja.get_attribute("value") == informacoes['nome_loja']:
            print("O nome da loja foi escrito corretamente")
        else:
            print("Ocorreu um erro ao escrever o nome da loja!")
            sys.exit()
        time.sleep(1)

        # Campo Nome Completo
        search_box_nomeCompleto = driver.find_element(By.XPATH, '//*[@id="frmCriarLoja"]/div/div/div[2]/div[1]/input')
        search_box_nomeCompleto.send_keys(informacoes['nome'])
        time.sleep(1)
        if search_box_nomeCompleto.get_attribute("value") == informacoes['nome']:
            print('O nome completo foi escrito corretamente')
        else:
            print("Ocorreu um erro ao escrever o nome completo!")
            sys.exit()
        time.sleep(1)

        # Campo Telefone
        search_box_telefone = driver.find_element(By.XPATH, '//*[@id="frmCriarLoja"]/div/div/div[2]/div[2]/input')
        search_box_telefone.send_keys(informacoes['telefone'])
        time.sleep(1)
        telefone_value = search_box_telefone.get_attribute("value")
        telefone_digits = ''.join(filter(str.isdigit, telefone_value))
        if telefone_digits == informacoes['telefone']:
            print("O número de telefone foi escrito corretamente!")
        else:
            print("Ocorreu um erro ao escrever o número de telefone!")
            sys.exit()

        time.sleep(1)

        # Campo Cidade
        search_box_cidade = driver.find_element(By.XPATH, '//*[@id="frmCriarLoja"]/div/div/div[3]/div[1]/input')
        search_box_cidade.send_keys(informacoes['cidade'])
        time.sleep(1)
        if search_box_cidade.get_attribute("value") == informacoes['cidade']:
            print("O nome da cidade foi escrito corretamente")
        else:
            print("Ocorreu um erro ao digitar o nome da cidade!")
            sys.exit()
        time.sleep(1)

        # Campo Estado
        select_box_estado = driver.find_element(By.XPATH, '//*[@id="frmCriarLoja"]/div/div/div[3]/div[2]/select')
        select = Select(select_box_estado)
        select.select_by_value(informacoes['estado'])
        time.sleep(2)
        if select_box_estado.get_attribute("value") == informacoes['estado']:
            print("O estado foi selecionado com sucesso!")
        else:
            print("Ocorreu um erro ao selecionar o estado")
            sys.exit()
        time.sleep(2)

        # Selecionar o Plano
        select_box_plano = driver.find_element(By.XPATH, '//*[@id="frmCriarLoja"]/div/div/div[4]/div/select')
        selectplano = Select(select_box_plano)

        if informacoes['plano'] == 'Starter':
            selectplano.select_by_value('21')
            time.sleep(1)
            if select_box_plano.get_attribute("value") != '21':
                print("Ocorreu um erro ao selecionar o plano! encerrando a execução")
                sys.exit()
            else: print("Foi selecionado o plano %s - %s com sucesso", select_box_plano.get_attribute('value'), informacoes['plano'])
        

        elif informacoes['plano'] == 'Advanced':
            selectplano.select_by_value('22')
            if select_box_plano != '22':
                print("Ocorreu um erro ao selecionar o plano! encerrando a execução")
                sys.exit()
            else: print("Foi selecionado o plano %s - %s com sucesso", select_box_plano.get_attribute('value'), informacoes['plano'])

        elif informacoes['plano'] == 'Professional':
            selectplano.select_by_value('26')
            if select_box_plano != '26':
                print("Ocorreu um erro ao selecionar o plano! encerrando a execução")
                sys.exit()
            else: print("Foi selecionado o plano %s - %s com sucesso", select_box_plano.get_attribute('value'), informacoes['plano'])

        elif informacoes['plano'] == 'Enterprise':
            selectplano.select_by_value('27')
            if select_box_plano != '27':
                print("Ocorreu um erro ao selecionar o plano! encerrando a execução")
                sys.exit()
            else: print("Foi selecionado o plano %s - %s com sucesso", select_box_plano.get_attribute('value'), informacoes['plano'])
        else:
            selectplano.select_by_value('28')
            if select_box_plano != '28':
                print("Ocorreu um erro ao selecionar o plano! encerrando a execução")
                sys.exit()
            else: print("Foi selecionado o plano %s - %s com sucesso", select_box_plano.get_attribute('value'), informacoes['plano'])

        time.sleep(2)

        # Campo Email
        search_box_email = driver.find_element(By.XPATH, '//*[@id="frmCriarLoja"]/div/div/div[6]/div/input')
        search_box_email.send_keys(informacoes['email'])
        time.sleep(1)
        if search_box_email.get_attribute("value") == informacoes['email']:
            print("O email foi inserido com sucesso")
        else:
            print("Ocorreu um erro ao inserir o email")
            sys.exit()
        time.sleep(1)

        # Repetir Email
        search_box_repeatEmail = driver.find_element(By.XPATH, '//*[@id="frmCriarLoja"]/div/div/div[7]/div[1]/input')
        search_box_repeatEmail.send_keys(informacoes['email'])
        time.sleep(1)
        if search_box_repeatEmail.get_attribute("value") == (informacoes['email']):
            print("O email foi inserido com sucesso!")
        else:
            print("Ocorreu um erro ao inserir o email")
            sys.exit()
        time.sleep(1)

        # Finalizar Registro
        finalizarRegistro = driver.find_element(By.XPATH, '//*[@id="frmCriarLoja"]/div/div/div[8]/div/button')
        finalizarRegistro.click()
        time.sleep(1)

        print('O cadastro foi realizado com sucesso')
        time.sleep(1)
        print("Passando para a proxima fase")

    #PROCESSO:
    #Após a realizar a primeira etapa de criação, a WBUY pede para que verifique o email com um codigo,
    #  e após tambem pede para verificar um SMS no celular, seleção de pessoa fisica ou juridica, colocar os dados, CPF data de nascimento e a seleção de objetivos
    #  após isso vem a etapa de colocar o cep endereço etc e finalizar cadastro
    
    #Após isso fazer a logica de receber o codigo da wbuy no gmail para realizar a verificação

    #Fazer a logica para recebimento do SMS no celular para a verificação da wbuy 
    finally:
    # Fechar o navegador
        driver.quit()


# LEITURA DO PDF
with open('C:/Users/Note/Desktop/Guilherme/BACKUPS/teste.pdf', 'rb') as input_pdf:
    print("Extraindo as informações do PDF, aguarde!")
    pdf_reader = PdfReader(input_pdf)

    num_pages = len(pdf_reader.pages)
    
    for page_number in range(num_pages):
        page = pdf_reader.pages[page_number]
        text = page.extract_text()
        
        informacoes = extrair_informacoes(text)
        if informacoes:
            print(f"Informações extraídas da página {page_number + 1}: {informacoes}")



# CONFIGURAÇÃO DO WEBDRIVER
edge_driver_path = 'C:/Users/Note/Desktop/edgedriver_win64/msedgedriver.exe'

prosseguir = input("Deseja realizar o cadastro? (sim/s): ").strip().lower()
if prosseguir == "sim" or prosseguir == "s":
    cadastrowBuy()
else:
    sys.exit()