
import os 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


import time

from Bromo.bromo import Bromo
from selenium.webdriver.common.by import By



class Interation:
    
    def __init__(self):

        service = Service(ChromeDriverManager(log_level=0).install())

        options = Options()
        options.add_argument(
                    f'user-data-dir={os.getcwd()}/Profile 1')
        #service = Service(executable_path='chromeself.driver.exe')
        self.driver = webdriver.Chrome(service=service, options=options)
        self.bromo = Bromo(self.driver)
        self.driver.get("https://casino.sportingbet.com/pt-br/games")


    def verificar_login(self):
        xpath_entrar ='/html/body/vn-app/vn-dynamic-layout-single-slot[2]/vn-responsive-header/header/nav/vn-header-section[2]/vn-h-button[1]/vn-menu-item/a/span'
        try:
            self.bromo.located(xpath_entrar, 5)
            return True
        except Exception as e:
            print(e)
            os.system('cls')
            print('login ja efetuado')
            return False
    
    
    def login(self, email = 'leandro2703palmeira@gmail.com', senha = 'Lps27031981'):
        try:
            click_entrar_js = 'document.querySelector("body > vn-app > vn-dynamic-layout-single-slot.slot.slot-single.slot-header > vn-responsive-header > header > nav > vn-header-section.navbar-wrapper-right > vn-h-button:nth-child(2) > vn-menu-item > a").click()'
            time.sleep(3)
            self.driver.execute_script(click_entrar_js)
    
            self.bromo.write('userId', email, method='id')
            
            senha_caixa_xpath = '//*[@id="password"]/input'
            time.sleep(3)
            self.bromo.write(senha_caixa_xpath, senha)
    
            time.sleep(3)
            entrar_xpath = '//*[@id="login"]/form/fieldset/section/div/button'

            entrar_js = 'document.querySelector("#login > form > fieldset > section > div > button").click()'
            #self.bromo.click(entrar_xpath)
            self.driver.execute_script(entrar_js)
        
        except Exception as e:
            print(e)
            print('erro no login')    
        
        
    def clicar_roleta(self):
        sala_click_js = 'document.querySelector("#gameIdentifier_homemostpopular_LiveDealerRoletaBrasil > div > div > a > cc-image-loader > div > img").click()'
        time.sleep(3)
        self.driver.execute_script(sala_click_js)
        
    
    def get_iframe(self, seletor, method = 'id'):
        
            time.sleep(10)
            if method == 'id':
                by = By.ID
            elif method == 'xpath':
                by = By.XPATH

            self.bromo.located(seletor,time = 30,  method=method)
            iframe_path = self.driver.find_element(by, seletor)
            self.driver.switch_to.frame(iframe_path)  

            return True
        
            '''except Exception as e:
            print(e)    
            return False
        '''
            
    def achar_numeros(self):
        try:
            numeros_xpath = '//*[@id="root"]/div[2]/div/div/div[7]/div/div[2]/div/div/div[4]'
        
            self.bromo.located(numeros_xpath, 20)
            numeros_html = self.driver.find_element(
                    By.XPATH, numeros_xpath).get_attribute('outerHTML')
                    
            return numeros_html
                
        except Exception as e:
            print('nao achou os numeros')
            print(e)
                
            return False
    
    
    def make_bet(self):
        even_xpath = '//*[@id="root"]/div[2]/div/div/div[7]/div/div[3]/div[3]/div/div[2]/div/div/div[1]/div/svg/g/rect[38]'
        even_xpath2 = '//*[@id="root"]/div[2]/div/div/div[7]/div/div[3]/div[3]/div/div[2]/div/div/div[1]/div/svg/g/rect[38]'
        path = '//*[@id="root"]/div[2]/div/div/div[7]/div/div[3]/div[3]/div/div[2]/div/div/div/div/svg/g/rect[38]'
        ficha_xpath ='//*[@id="root"]/div[2]/div/div/div[7]/div/div[4]/div/div[2]/div/div[1]'
        #self.bromo.located(ficha_xpath, time = 30)
        class_xpath ='baseGrid--7ec7f'
        self.bromo.located(class_xpath, method='class', time = 60)
        path_js = 'document.querySelector("#root > div.app--2c5f6 > div > div > div.footerWrapper--3a742 > div > div.perspectiveContainer--b459a > div.bettingGrid--217c5 > div > div.perspectiveContainer--87027 > div > div > div.svg-wrapper--86340 > div > svg > g > text:nth-child(199)").click()'
        #self.driver.execute_script(path_js)
        try:
            self.bromo.click(even_xpath, time=60)
        except Exception as e:
            os.system('cls')
            print('não foi o primeiro')    
        
        self.bromo.click(even_xpath2, time=60)
        return True
        
        
    
    def bet_value_mais(self):
        mais_xpath_button = '//*[@id="root"]/div[2]/div/div/div[7]/div/div[2]/div/div/div[5]/div[2]/div/svg/polygon'
        self.bromo.click(mais_xpath_button, time=20)
        return True
    
    def bet_value_menos(self):
        menos_xpath_button = '//*[@id="root"]/div[2]/div/div/div[7]/div/div[2]/div/div/div[5]/div[2]/div/svg/circle[2]'
        
        self.bromo.click(menos_xpath_button)
        
        return True
        
        pass
    
    def bet_value_js(self):
        mais_js = 'document.querySelector("#root > div.app--2c5f6 > div > div > div.footerWrapper--3a742 > div > div.footerRight--5d28e > div > div > div.racetrackContainer--33a9a > div.racetrackNeighbourPicker--c4f82 > div > svg > circle.plus--4a8fc").click()'
        self.driver.execute_script(mais_js)
    
    
    def make_bet_odd(self):
        odd_xpath = '//*[@id="root"]/div[2]/div/div/div[7]/div/div[3]/div[3]/div/div[2]/div/div/div[1]/div/svg/g/rect[37]'
        self.bromo.click(odd_xpath)
        print('posta no odd feita')
        return True
    
        
    def make_bet_even(self):
        even_xpath = '//*[@id="root"]/div[2]/div/div/div[7]/div/div[3]/div[3]/div/div[2]/div/div/div[1]/div/svg/g/rect[38]'
        self.bromo.click(even_xpath)
        print('posta no even feita')
        return True
        
        
    def verify_bet(self):
        pass
        
        
    def martingales(self, value, multiplicator):
        
        value_gale = float(value)*float(multiplicator)
        
        return value_gale
        
        
        
    
    


if __name__ == '__main__':
    
    interation = Interation()
    if interation.verificar_login() == True:
            print('vai fazer login')
            interation.login('coelhoembaixadormagico@gmail.com','Aulabot1')
    os.system('cls')
    interation.clicar_roleta()
    interation.get_iframe('embedGameIframe')
    print('primeiro iframe')
    interation.get_iframe('vendor-LiveDealerRoletaBrasil')
    
    print('segundo iframe')
    interation.make_bet()
    
    print('fez a aposta foi')
    pass
    #time.sleep(15)



    #os.system('cls')
    # 1: fechar o popup
    input('sair')
    #login()
