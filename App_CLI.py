#!/usr/bin/env python

__author__ = 'Visto-Preto'

import os, sqlite3, sys
from datetime import datetime
from module.realsymbol import Real as rs
from App import Control_DB

user = sys.argv[1]
passwd = sys.argv[2]

Control_DB.ver(user, passwd, '')
conta = rs.float_to_s((Control_DB.v_conta(user)))
ultvalor, tipo, ultdata, extrato = Control_DB.ultrow(user)
ultvalor =  rs.float_to_s(ultvalor)

red = '\033[1;31m'
green = '\033[1;32m'
yellow = '\033[1;33m'
blue = '\033[1;34m'
magenta = '\033[1;35m'
cyan = '\033[1;36m'
cls = '\033[m'

def menu_conta(y, z):
    menu = '''
{}================================================
               {}CAIXA DE ECONOMIAS           
{}================================================
 {}Usuário: {}{}
{}================================================
{}------------------------------------------------
 {}DATA: {}{}                {}HORA: {}{}
{}------------------------------------------------
 {}UltM: {}|{}{}{}| |{}{}{}| {}{}
{}------------------------------------------------
 {}Valor em conta: {}{}
{}------------------------------------------------
{}================================================{}
'''.format( green, 
            blue, 
            green,
            yellow,
            cyan,
            y,
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
            tipo, 
            magenta, 
            red, 
            ultdata, 
            magenta, 
			
            green, 
            ((16 - len(ultvalor)) * ' ' + ultvalor), 
            magenta, 
            yellow, 
            green, 
            ((30 - len(conta)) * ' ' + conta), 
            magenta, 
            green, 
            cls)
    print(menu)

    print(' {}01{}]    {}Depositar'.format(blue,cls, yellow))
    print(' {}02{}]    {}Sacar'.format(blue,cls, yellow))
    print(' {}03{}]    {}Extrato'.format(blue,cls, yellow))
    print(' {}00{}]    {}Sair'.format(blue,cls, yellow))
    print('')
    print('{}================================================{}'.format(green, cls))
    print('')
    rsp = str(input(' {}Entre com o numero da opção:\n\n {}~/{}Terminal{} $ '.format(blue, green, yellow, cls)))
    
    if rsp == '00':
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
        menu_conta(user, passwd)

if __name__ == ('__main__'):
	menu_conta(user, passwd)
