import time
import data
from interation import Interation


class Roulette:
        
    def __init__(self):
        self.interation = Interation()
        
        self.initial_branking = self.banking()
                
    
    def inicialize_page(self):
        print('vai verificar o login')
        if self.interation.verificar_login() == True:
            print('vai fazer login')
            self.interation.login('coelhoembaixadormagico@gmail.com','Aulabot1')

        self.interation.clicar_roleta()
        #achar_iframe()
        self.interation.get_iframe('embedGameIframe')
        print('iframe 1')
        self.interation.get_iframe('vendor-LiveDealerRoletaBrasil')
        print('iframe 2')
        #self.interation.get_iframe('/html/body/div[6]/div[1]/iframe', method='xpath')
        #print('iframe 3')
    
    
    def banking(self):
        banking_html = self.interation.get_banking()
        value = data.banking_value(banking_html)
        return value
    
    
    def make_bet_odd(self, apostas, delay):
        self.interation.make_bet('even', apostas, delay)
        return True
    
        
    def make_bet_even(self, apostas, delay=0.8):
        self.interation.make_bet('even', apostas, delay)
        return True
    
    
    def make_bet_black(self, apostas, delay=0.8):
        self.interation.make_bet('black', apostas, delay)
        return True
                   
    
    def make_bet_red(self, apostas, delay=0.8):
        self.interation.make_bet('red', apostas, delay)
    
    def get_numbers_history(self):
        numbers_html = self.interation.achar_numeros()
        numbers = data.tratar_numeros(numbers_html)
        
        return numbers

    def verify_bet(self):
        self.interation.verify_bet
        self.current_baking = self.banking()
        return self.current_baking
    
    
    def estrategy_even_odd(self):
        self.inicialize_page()
        print('carregou a pagina')
        
        numbers = self.get_numbers_history()
        print(numbers)
        diretion = data.verify_entrada(numbers)
        print(diretion)
        
        if diretion == 'odd':
            self.make_bet_odd()
            
        elif diretion == 'even':
            self.make_bet_even()
        pass
        
        
    def run(self):
        
        
        

        
        
        
       
        
        
        
        
        self.interation.make_bet(1)
        


        time.sleep(15)



    #os.system('cls')
    # 1: fechar o popup
 

    

if __name__ == '__main__':
    
    roleta = Roulette()
    roleta.run()
    input('sair')

    