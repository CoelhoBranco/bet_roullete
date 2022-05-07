import time

from data import ProcessData
from interation import Interation



if __name__ == '__main__':
    interation = Interation()
    data =  ProcessData()

    print('vai verificar o login')
    if interation.verificar_login() == True:
        print('vai fazer login')
        interation.login('coelhoembaixadormagico@gmail.com','Aulabot1')

    interation.clicar_roleta()
    #achar_iframe()
    interation.get_iframe('embedGameIframe')
    interation.get_iframe('vendor-LiveDealerRoletaBrasil')
    interation.get_iframe('/html/body/div[6]/div[1]/iframe', method='xpath')
    
    numeros = interation.achar_numeros()
    
    data.tratar_numeros(numeros)
    
    
    time.sleep(15)



    #os.system('cls')
    # 1: fechar o popup
    input('sair')
