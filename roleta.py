import time


import data
import pandas as pd
from interation import Interation


class Roulette:
        
    def __init__(self):
        self.interation = Interation()
        
        
        
        self.df = pd.read_csv('parametros.csv')
                
    
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
    
    
    def make_bet_odd(self, apostas, confidence=0.7, delay=0.8):
        self.interation.make_bet('odd', apostas,confidence, delay)
        return True
    
        
    def make_bet_even(self, apostas, confidence=0.7, delay=0.8):
        self.interation.make_bet('even', apostas,confidence, delay)
        return True
    
    
    def make_bet_black(self, apostas, confidence=0.7, delay=0.8):
        self.interation.make_bet('black', apostas,confidence, delay)
        return True
                   
    
    def make_bet_red(self, apostas, confidence=0.7, delay=0.8):
        self.interation.make_bet('red', apostas,confidence, delay)
    
    
    def get_numbers_history(self):
        numbers = False
        numbers_html = self.interation.achar_numeros()
        if type(numbers_html) != bool:
            numbers = data.tratar_numeros(numbers_html)        
        return numbers

    def verify_bet_inutilizado(self):
        self.interation.verify_bet()
        self.current_baking = self.banking()
        return self.current_baking
    
    
    def make_gale(self, bet):
        value_bet = data.martingale_value(bet)
        return value_bet
          
    
    def verify_result_estrategy(self, number, diretion):
        if diretion == number:
            return 'Loss'
                
        if diretion != number:
            return "Gain"
          
    
    def verify_even_odd(self, numbers, diretion):
        while True:
            last_numbers = self.get_numbers_history()
            
            if last_numbers != numbers:
                number = data.verify_eo(numbers)
                return self.verify_result_estrategy(number, diretion)
                                
            else:
                time.sleep(3)
                     
    
    def verify_black_white(self, numbers, color):
        while True:
            last_numbers = self.get_numbers_history()
            
            if last_numbers != numbers:
                color_verify = data.verify_br(numbers)
                return self.verify_result_estrategy(color_verify, color)
                
            else:
                time.sleep(3)
                             
    
    def estrategy_even_odd(self):
        self.inicialize_page()
        print('carregou a pagina')
                      
        while True:
            numbers = self.get_numbers_history()
            print(f'numeros = {numbers}')
            
            if type(numbers) != bool:
                diretion = data.verify_entrada(numbers)
            
                print(f'direção: {diretion}')
            
            bet = data.initial_bet()
            
            if diretion != False:
                
                while True:
                    if diretion == 'even':
                        self.make_bet_odd(bet)
                        
                    elif diretion == 'odd':
                        self.make_bet_even(bet)
                    
                    result = self.verify_even_odd(numbers, diretion)
                    
                    if result == 'Loss':
                        bet = self.make_gale(bet)
                        
                    elif result == 'Gain':
                        break
      
            else:
                continue    
            
    
    def estrategy_red_black(self):
        self.inicialize_page()
        print('carregou a pagina')
        
        color = data.option_bet()
        bet = data.initial_bet()
        
        while True:
            numbers = self.get_numbers_history()
            while True:
            
                if color == 'red':
                    self.make_bet_black(bet)

                elif color == 'black': 
                    self.make_bet_red(bet)

                result = self.verify_black_white(numbers, color)
                    
                if result == 'Loss':
                    bet = self.make_gale(bet)
                        
                elif result == 'Gain':
                
                    if color == 'black':
                        color = 'red'

                    elif color == 'red':
                        color = 'black'

                    break
                   
        
    def run(self):
        estrategy = data.estrategy()
        
        if estrategy == 0:
            self.estrategy_even_odd()
        
        elif estrategy == 1:
            self.estrategy_red_black()
        
        


    #os.system('cls')
    # 1: fechar o popup
 

    

if __name__ == '__main__':
    
    roleta = Roulette()
    #roleta.run()
    roleta.verify_black_white([2], 'red')
    input('sair')

    