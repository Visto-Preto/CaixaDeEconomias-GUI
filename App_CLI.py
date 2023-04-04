#!/usr/bin/env python

__author__ = 'Visto-Preto'

import os, sqlite3, sys
from datetime import datetime
from module.realsymbol import Real as rs
from App import Control_DB
from module import platform

path_main, path_db, os_cls, red, green, yellow, blue, magenta, cyan, reset = platform.platform()

user = sys.argv[1]
passwd = sys.argv[2]

Control_DB.ver(user, passwd, '')
conta = rs.float_to_s((Control_DB.v_conta(user)))
ultvalor, tipo, ultdata, extrato = Control_DB.ultrow(user)
ultvalor =  rs.float_to_s(ultvalor)


def f_extrato(x):
    os.system(os_cls)
    print('{}================================================{}'.format(green, reset))
    print('               {}CAIXA DE ECONOMIAS{}            '.format(blue, reset))
    print('{}================================================{}'.format(green, reset))
    print(' {}Usuário: {}{}{}'.format(yellow, cyan, user, reset))
    print('{}================================================{}'.format(green, reset))
    print('{}------------------------------------------------{}'.format(magenta,reset))
    print('{} Extratos de movimentação{}'.format(yellow, reset))
    print('{}------------------------------------------------{}'.format(magenta, reset))
    for i in x:
        v_ex = rs.float_to_s(i[2])
        print(' {}|{}{}{}| |{}{}{}| {}{}{}'.format(magenta, blue, i[1], magenta, blue, i[0], magenta, green, ((22 - len(v_ex)) * ' ' + v_ex), reset))
        print('')
        print(' {}Desc: {}{}{}'.format(yellow, cyan, i[3], reset))
        print('{}------------------------------------------------{}'.format(magenta, reset))
    print('{}================================================{}'.format(green, reset))
    print(' {}Valor em conta: {}{}{}'.format(yellow, green, ((30 - len(conta)) * ' ' + conta), reset ))
    print('{}================================================{}'.format(green, reset))
    print('')
    print(' {}01{}]    {}Terminal'.format(blue,reset, yellow))
    print(' {}00{}]    {}Sair'.format(blue,reset, yellow))
    print('')
    print('{}================================================{}'.format(green, reset))
    print('')
    rsp = str(input(' {}Entre com o numero da opção:\n\n {}~/{}Terminal{} $ '.format(blue, green, yellow, reset)))
    
    if rsp == '00':
        os.system(os_cls)
    elif rsp == '01':
        os.system(os_cls)
        menu_conta(user, passwd)
    else:
        os.system(os_cls)
        f_extrato(extrato)


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
            blue, 
            tipo, 
            magenta, 
            blue, 
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
            reset)
    os.system(os_cls)
    print(menu)

    print(' {}01{}]    {}Depositar'.format(blue,reset, yellow))
    print(' {}02{}]    {}Sacar'.format(blue,reset, yellow))
    print(' {}03{}]    {}Extrato'.format(blue,reset, yellow))
    print(' {}04{}]    {}Deletar conta'.format(blue,reset, yellow))
    print(' {}00{}]    {}Sair'.format(blue,reset, yellow))
    print('')
    print('{}================================================{}'.format(green, reset))
    print('')
    rsp = str(input(' {}Entre com o numero da opção:\n\n {}~/{}Terminal{} $ '.format(blue, green, yellow, reset)))
    
    if rsp == '00':
        os.system(os_cls)
    elif rsp == '01':
        os.system(os_cls)
        main(depositar)
    elif rsp == '02':
        os.system(os_cls)
        main(sacar)
    elif rsp == '03':
        os.system(os_cls)
        f_extrato(extrato)
    else:
        menu_conta(user, passwd)

if __name__ == ('__main__'):
	menu_conta(user, passwd)
