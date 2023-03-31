#!/usr/bin/env python
#coding: utf-8
__author__ = 'Visto-Preto'

import os, sqlite3, sys
from datetime import datetime
from module.realsymbol import Real as rs
from module import menus_cli
from App import Control_DB

user = sys.argv[1]
passwd = sys.argv[2]

red = '\033[1;31m'
green = '\033[1;32m'
yellow = '\033[1;33m'
blue = '\033[1;34m'
magenta = '\033[1;35m'
cyan = '\033[1;36m'
cls = '\033[m'


def mainop():
    print('{}01{}]    {}Depositar'.format(blue,cls, yellow))
    print('{}02{}]    {}Sacar'.format(blue,cls, yellow))
    print('{}03{}]    {}Extrato'.format(blue,cls, yellow))
    print('{}00{}]    {}Sair'.format(blue,cls, yellow))
    print('')
    print('{}================================================{}'.format(green, cls))
    print('')
    rsp = str(input('{}Entre com o numero da opção:\n\n{}~/{}Terminal{} $ '.format(blue, green, yellow, cls)))
   
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
        menus_cli.menu_conta(mainop, user, passwd)
        
if __name__ == ('__main__'):
    menus_cli.menu_conta(mainop, user, passwd)