from bs4 import BeautifulSoup



def tratar_numeros(self, dados):
    soup = BeautifulSoup(dados, 'html.parser')
    numeros_html = soup.find_all(class_="value--877c6")
    lista_numeros = numeros_html[:-1]
    
    lista_numeros_tratados = []
    for numero in lista_numeros:
        
        numero = numero.text
        lista_numeros_tratados.append(numero)
    
    return lista_numeros_tratados


def banking_value(self, data):
    soup = BeautifulSoup(data, 'html.parser')
    span_html = soup.find_all('span')
    for span in span_html:
        try:
            if span.attrs['data-role'] == 'balance-label__value':
                value = span.text
                return int(value)
        except:
            pass


def estrategy_verify(self, number):
    if number%2 == 0 :
        return True
    else:
        return False
    
    
def verify_entrada(self, numbers, unidades=4):
    odd_list = []
    even_list = []
    if len(numbers) > 4:
        for number in numbers[0:int(unidades)]:
            number = float(number)
            print(number)
            if self.estrategy_verify(number) == True:
                even_list.append(number)

            else:
                odd_list.append(number)

            if len(odd_list) != 0 and len(even_list) != 0:
                print('quebrou a estrategia')
                return False
            
        if len(even_list) != 0 and len(odd_list) == 0:
            return 'even'
        
        elif len(odd_list) != 0 and len(even_list) == 0:
            return 'odd'
            
        
    
            
            
        else:
            return False    
                
        
        
        pass
    
if __name__ == '__main__':
    with open('numeros_atualizado.html', 'r') as html:
        html = html.read()
        
    #data = ProcessData()
    #numeros = data.tratar_numeros(html)
    numeros = ['28', '26', '2', '25', '14', '14', '28', '23', '24', '7', '12']
    verify_entrada(numeros)
    #print(numeros)