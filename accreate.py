from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

# LEITURA DO PDF



#DECLARAÇÃO DAS INFOS


edge_driver_path = 'C:/Users/Note/Desktop/edgedriver_win64/msedgedriver.exe'
edge_options = EdgeOptions()
edge_service = EdgeService(executable_path=edge_driver_path)

driver = webdriver.Edge(service=edge_service, options=edge_options)

try:
    driver.get("https://www.wbuy.com.br/criar-loja-virtual/")
    time.sleep(2)
    
    # Campo Nome da sua Loja
    search_box_nomeLoja = driver.find_element(By.XPATH, '//*[@id="frmCriarLoja"]/div/div/div[1]/div/input')
    search_box_nomeLoja.send_keys('Loja Virtual Teste')
    time.sleep(2)
    if search_box_nomeLoja.get_attribute("value") == 'Loja Virtual Teste':
        print("O nome da loja foi escrito corretamente")
    else:
        print("Ocorreu um erro ao escrever o nome da loja!")
    time.sleep(2)

    # Campo Nome Completo
    search_box_nomeCompleto = driver.find_element(By.XPATH, '//*[@id="frmCriarLoja"]/div/div/div[2]/div[1]/input')
    search_box_nomeCompleto.send_keys('Testando da Silva')
    time.sleep(2)
    if search_box_nomeCompleto.get_attribute("value") == 'Testando da Silva':
        print('O nome completo foi escrito corretamente')
    else:
        print("Ocorreu um erro ao escrever o nome completo!")
    time.sleep(2)

    # Campo Telefone
    search_box_telefone = driver.find_element(By.XPATH, '//*[@id="frmCriarLoja"]/div/div/div[2]/div[2]/input')
    search_box_telefone.send_keys('15993735471')
    time.sleep(2)
    if search_box_telefone.get_attribute("value") == '(15)99373-5471':
        print("O número de telefone foi escrito corretamente!")
    else:
        print("Ocorreu um erro ao escrever o número de telefone!")
    time.sleep(2)

    # Campo Cidade
    search_box_cidade = driver.find_element(By.XPATH, '//*[@id="frmCriarLoja"]/div/div/div[3]/div[1]/input')
    search_box_cidade.send_keys('Sorocaba')
    time.sleep(2)
    if search_box_cidade.get_attribute("value") == 'Sorocaba':
        print("O nome da cidade foi escrito corretamente")
    else:
        print("Ocorreu um erro ao digitar o nome da cidade!")
    time.sleep(2)

    # Campo Estado
    select_box_estado = driver.find_element(By.XPATH, '//*[@id="frmCriarLoja"]/div/div/div[3]/div[2]/select')
    select = Select(select_box_estado)
    select.select_by_value("SP")
    time.sleep(2)
    if select_box_estado.get_attribute("value") == 'SP':
        print("O estado foi selecionado com sucesso!")
    else:
        print("Ocorreu um erro ao selecionar o estado")
    time.sleep(2)

    # Selecionar o Plano
    select_box_plano = driver.find_element(By.XPATH, '//*[@id="frmCriarLoja"]/div/div/div[4]/div/select')
    selectplano = Select(select_box_plano)
    selectplano.select_by_value("21")  # O valor deve ser uma string
    time.sleep(2)
    if select_box_plano.get_attribute("value") == "21":  # Comparar com string
        print("O plano foi selecionado com sucesso!")
    else:
        print("Ocorreu um erro ao selecionar o plano")
    time.sleep(2)

    # Campo Email
    search_box_email = driver.find_element(By.XPATH, '//*[@id="frmCriarLoja"]/div/div/div[6]/div/input')
    search_box_email.send_keys('testemail@gmail.com')
    time.sleep(2)
    if search_box_email.get_attribute("value") == 'testemail@gmail.com':
        print("O email foi inserido com sucesso")
    else:
        print("Ocorreu um erro ao inserir o email")
    time.sleep(2)

    # Repetir Email
    search_box_repeatEmail = driver.find_element(By.XPATH, '//*[@id="frmCriarLoja"]/div/div/div[7]/div[1]/input')
    search_box_repeatEmail.send_keys("testemail@gmail.com")
    time.sleep(2)
    if search_box_repeatEmail.get_attribute("value") == 'testemail@gmail.com':
        print("O email foi inserido com sucesso!")
    else:
        print("Ocorreu um erro ao inserir o email")
    time.sleep(2)

    # Finalizar Registro
    finalizarRegistro = driver.find_element(By.XPATH, '//*[@id="frmCriarLoja"]/div/div/div[8]/div/button')
    finalizarRegistro.click()
    time.sleep(2)

    print('O cadastro foi realizado com sucesso')
    time.sleep(2)
    print("Passando para a proxima fase")
finally:
    # Fechar o navegador
    driver.quit()
