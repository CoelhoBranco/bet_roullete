import os 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

import time

from Bromo.bromo import Bromo
from selenium.webdriver.common.by import By

#service = Service(executable_path='chromedriver.exe')
service = Service(ChromeDriverManager(log_level=0).install())

options = Options()


options.add_argument(
           f'user-data-dir={os.getcwd()}/Profile 1')
# passo 0 : navegar até o site

#abre o navegador
driver = webdriver.Chrome(service=service, options=options)
driver.get("https://casino.sportingbet.com/pt-br/games")

bromo = Bromo(driver)
os.system('cls')
# 1: fechar o popup

def fechar_popup():
    fechar_popup_xpath = '//*[@id="messages-with-overlay"]/div/vn-content-message/div/span'
    time.sleep(10)
    bromo.click(fechar_popup_xpath, time=60)

#time.sleep(30)

#driver.execute_script('document.querySelector("#messages-with-overlay > div > vn-content-message > div > span").click()')
#//*[@id="messages-with-overlay"]/div/vn-content-message/div/span
#messages-with-overlay > div > vn-content-message > div > span


# 2 clicar no loginr

def verificar_login():
    xpath_entrar ='/html/body/vn-app/vn-dynamic-layout-single-slot[2]/vn-responsive-header/header/nav/vn-header-section[2]/vn-h-button[1]/vn-menu-item/a/span'
    try:
        bromo.located(xpath_entrar, 5)
        return True
    except Exception as e:
        print(e)
        print('login ja efetuado')
        return False

def login(email = 'leandro2703palmeira@gmail.com', senha = 'Lps27031981'):
    try:
        click_entrar = 'document.querySelector("body > vn-app > vn-dynamic-layout-single-slot.slot.slot-single.slot-header > vn-responsive-header > header > nav > vn-header-section.navbar-wrapper-right > vn-h-button:nth-child(2) > vn-menu-item > a").click()'
        time.sleep(3)
        driver.execute_script(click_entrar)

        #time.sleep(20)

        # 3 fazer o login geral 
    
        bromo.write('userId', email, method='id')

        senha_caixa_xpath = '//*[@id="password"]/input'

        time.sleep(3)
        bromo.write(senha_caixa_xpath, senha)

        time.sleep(3)
        entrar_xpath = '//*[@id="login"]/form/fieldset/section/div/button'

        entrar_js = 'document.querySelector("#login > form > fieldset > section > div > button").click()'

        #bromo.click(entrar_xpath)
        driver.execute_script(entrar_js)
    except Exception as e:
        print(e)
        print('erro no login')    
    



print('vai verificar o login')
if verificar_login() == True:
    print('vai fazer login')
    login()

sala_click_js = 'document.querySelector("#gameIdentifier_homemostpopular_LiveDealerRoletaBrasil > div > div > a > cc-image-loader > div > img").click()'
time.sleep(3)
driver.execute_script(sala_click_js)

"""
ATENÇÃOOOOOO

"""

iframe_xpath = '//*[@id="vendor-LiveDealerRoletaBrasil"]'
numeros_xpath = '//*[@id="root"]/div[2]/div/div/div[7]/div/div[2]/div/div/div[4]'
#numeros_xpath = '//numeros'
#while True:
try:
    
        with open('scraper.js', 'r') as js:
            #js_code = js.read()
            pass
            
        #driver.execute_script(js_code)
        # Pega o XPath do iframe e atribui a uma variável
        try:
            bromo.located(iframe_xpath, 60)
            iframe = driver.find_element(By.XPATH, iframe_xpath)
        except Exception as e:
            print('erro ao achar o iframe')
# Muda o foco para o iframe
        driver.switch_to.frame(iframe)
        numeros_html = driver.find_element(By.XPATH, numeros_xpath).get_attribute('outerHTML')
# Retorna para a janela principal (fora do iframe)
        driver.switch_to.default_content()
        print(0)
        #time.sleep(60)
        '''for _ in range(5):
            try:
                bromo.located(numeros_xpath, time=20, method='xpath')
                break
            except Exception as e:
                os.system('cls')
                print(e)
        print(1)'''
        try:
            pass
        except Exception as e:
            os.system('cls')
            print(e)
            print('erro no numeros')
            
        
        '''with open('numeros_atualizados.html', 'a') as html:
            html.write(numeros_html) ''' 
            
        soup = BeautifulSoup(numeros_html, 'html.parser')

        numeros_html = soup.find_all(class_="value--877c6")
        lista_numeros = numeros_html[:4]
        lista_numeros_tratados = []
        print(2)
        for numero in lista_numeros:
            #print(numero.text)
            numero = numero.text
            lista_numeros_tratados.append(numero)
        print(lista_numeros_tratados)
        
        print('terminou')
#        break
except Exception as erro:
        print(erro)
        print('erro maior')
        time.sleep(10)
        #driver.refresh()

'''def entrada_numero_impar():
        
        pass'''
        
'''
    numeros pares?
    if numeros_pares == 4:
        entrada_numero_impar()
        
        while True:
            verificar o numero
            
            if perdeu == True:
                gale()
                
            else:
                pass
            
        
        
    else:
        pass


        





'''

input('sair')

