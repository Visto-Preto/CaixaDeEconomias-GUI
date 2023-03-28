#!/usr/bin/env python
#coding: utf-8
__author__ = 'Visto-Preto'

import os, sqlite3
from datetime import datetime
from module.realsymbol import Real as rs

red = '\033[1;31m'
green = '\033[1;32m'
yellow = '\033[1;33m'
blue = '\033[1;34m'
magenta = '\033[1;35m'
cyan = '\033[1;36m'
cls = '\033[m'



menu = '''
{}================================================
               {}CAIXA DE ECONOMIAS           
{}================================================
{}------------------------------------------------
{}DATA: {}{}                {}HORA: {}{}
{}------------------------------------------------
{}UltM: {}|{}{}{}| |{}{}{}|{} {}{}
{}------------------------------------------------
{}Valor em conta: {}{}
{}------------------------------------------------
{}================================================{}'''.format( green, 
                                                                blue, 
                                                                green, 
                                                                magenta, 
                                                                yellow, 
                                                                cyan, 
                                                                datetime.today().strftime('%d/%m/%Y'),
                                                                yellow, 
                                                                cyan, 
                                                                datetime.today().strftime('%H:%M:%S'),       
                                                                magenta, 
                                                                yellow , 
                                                                magenta, 
                                                                red, 
                                                                'Valor 1', 
                                                                magenta, 
                                                                red, 
                                                                'Valor 2', 
                                                                magenta, 
                                                                'Valor 3', 
                                                                green, 
                                                                ((16 - len('Valor 4')) * ' ' + 'Valor 4'), 
                                                                magenta, 
                                                                yellow, 
                                                                green, 
                                                                ((30 - len('Valor 5')) * ' ' + 'Valor 5'), 
                                                                magenta, 
                                                                green, 
                                                                cls)
print(menu)



def mainop():
 
    print('{}01{}]    {}Depositar'.format(blue,cls, yellow))
    print('{}02{}]    {}Sacar'.format(blue,cls, yellow))
    print('{}03{}]    {}Extrato'.format(blue,cls, yellow))
    print('{}00{}]    {}Sair'.format(blue,cls, yellow))
    print('{}================================================{}'.format(green, cls))
    print()
    rsp = str(input('{}Entre com o numero da opção:\n\n{}~/{}Terminal{} $ '.format(blue, green, yellow, cls)))
   
    if rsp == '00':
        os.system('termux-vibrate -d 100')
        os.system('clear')
    elif rsp == '01':
        os.system('clear')
        main(depositar)
    elif rsp == '02':
        os.system('clear')
        main(sacar)
    elif rsp == '03':
        os.system('clear')
        main(extrato)
    else:
        main(mainop)
        
if __name__ == ('__main__'):
    mainop()