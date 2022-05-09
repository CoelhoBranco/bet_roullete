import time
import pandas as pd
from bs4 import BeautifulSoup



df = pd.read_csv('parametros.csv', delimiter=';')

def initial_bet():
    value = df.loc[0,'valor_inicial']
    return value
    

def option_bet():  
    value = df.loc[0,'red/black']
    return value


def estrategy():
    return df.loc[0,'(odd/even)(red/black)(0/1)']
    pass


def tratar_numeros(dados):
    
    soup = BeautifulSoup(dados, 'html.parser')
    numeros_html = soup.find_all(class_="value--877c6")
    lista_numeros = numeros_html[:-1]
    
    lista_numeros_tratados = []
    for numero in lista_numeros:
        
        numero = numero.text
        lista_numeros_tratados.append(numero)
    
    return lista_numeros_tratados


def verify_eo(numbers):
    gain = numbers[0]
    
    if estrategy_verify(gain) == True:
        return 'even'
    
    elif estrategy_verify(gain) == False:
        return 'odd'
    
    
def verify_br(numbers):
    numbers = int(numbers[0])
    color = {
    1: 'red',
    2: 'black',
    3: 'red',
    4: 'black',
    5: 'red',
    6: 'black',
    7: 'red',
    8: 'black',
    9: 'red',
    10: 'black',
    11: 'black',
    12: 'red',
    13: 'black',
    14: 'red',
    15: 'black',
    16: 'red',
    17: 'black',
    18: 'red',
    19: 'red',
    20: 'black',
    21: 'red',
    22: 'black',
    23: 'red',
    24: 'black',
    25: 'red',
    26: 'black',
    27: 'red',
    28: 'black',
    29: 'black',
    30: 'red',
    31: 'black',
    32: 'red',
    33: 'black',
    34: 'red',
    35: 'black',
    36: 'red'}
    
    return color[numbers]
    
    

def banking_value(data):
    soup = BeautifulSoup(data, 'html.parser')
    span_html = soup.find_all('span')
    for span in span_html:
        try:
            if span.attrs['data-role'] == 'balance-label__value':
                value = span.text
                return int(value)
        except:
            pass


def estrategy_verify(number):
    number = int(number)
    if number%2 == 0 :
        return True
    else:
        return False
    

def martingale_value(value):
    
    multiplicator = df.loc[0,'multiplicador']
    
    value_gale = float(value)*float(multiplicator)
    return value_gale

    
def verify_entrada(numbers, unidades=4):
    odd_list = []
    even_list = []
    if len(numbers) > 4:
        for number in numbers[0:int(unidades)]:
            number = float(number)
            print(number)
            if estrategy_verify(number) == True:
                even_list.append(number)

            else:
                odd_list.append(number)

            if len(odd_list) != 0 and len(even_list) != 0:
                print('quebrou a estrategia')
                time.sleep(15)
                return False
            
        if len(even_list) != 0 and len(odd_list) == 0:
            return 'even'
        
        elif len(odd_list) != 0 and len(even_list) == 0:
            return 'odd'
       
            
        else:
            return False    

    
if __name__ == '__main__':
        
    #data = ProcessData()
    #numeros = data.tratar_numeros(html)
    numeros = ['27', '26', '2', '25', '14', '14', '28', '23', '24', '7', '12']
    result = verify_br(numeros)
    print(result)
    #print(numeros)