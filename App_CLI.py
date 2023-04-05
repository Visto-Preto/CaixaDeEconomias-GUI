#!/usr/bin/env python

__author__ = 'Visto-Preto'

import os, sqlite3, sys, time
from datetime import datetime
from module.realsymbol import Real as rs
from App import Control_DB
from module import platform

path_main, path_db, os_cls, red, green, yellow, blue, magenta, cyan, reset, delete = platform.platform()

user = sys.argv[1]
passwd = sys.argv[2]

Control_DB.ver(user, passwd, '')
conta = rs.float_to_s((Control_DB.v_conta(user)))
ultvalor, tipo, ultdata, extrato = Control_DB.ultrow(user)
ultvalor =  rs.float_to_s(ultvalor)

def delete():
    con = sqlite3.connect(path_db + user + '.db')
    cur = con.cursor()
    for pswd_db in cur.execute('''SELECT pswd FROM dados_login'''):
        pswd_db = pswd_db[0]
    os.system(os_cls)
    print('{}================================================{}'.format(green, reset))
    print('               {}CAIXA DE ECONOMIAS{}            '.format(blue, reset))
    print('{}================================================{}'.format(green, reset))
    print(' {}Usuário: {}{}{}'.format(yellow, cyan, user, reset))
    print('{}================================================{}'.format(green, reset))
    print('{}------------------------------------------------{}'.format(magenta,reset))
    print('{} Exclusão de conta{}'.format(yellow, reset))
    print('{}------------------------------------------------{}'.format(magenta, reset))
    print('')
    rsp = str(getpass.getpass(' {}Entre com o password:\n\n {}~/{}Terminal{} $ '.format(blue, green, yellow, reset)))
    if rsp == pswd_db:
        os.system('{} {}{}.db'.format(delete, path_db, user))
        os.system(os_cls)
        print(' {}Conta excluida com sucesso.{}'.format(red, reset))
        time.sleep(0.5) 
    else:
        os.system(os_cls)
        print(' {}senha incorreta.{}'.format(red, reset))
        time.sleep(0.5) 

def saque():
    def mov():
        os.system(os_cls)
        print('{}================================================{}'.format(green, reset))
        print('               {}CAIXA DE ECONOMIAS{}            '.format(blue, reset))
        print('{}================================================{}'.format(green, reset))
        print(' {}Usuário: {}{}{}'.format(yellow, cyan, user, reset))
        print('{}================================================{}'.format(green, reset))
        print('{}------------------------------------------------{}'.format(magenta,reset))
        print('{} Saque {}'.format(yellow, reset))
        print('{}------------------------------------------------{}'.format(magenta, reset))
        print('{}================================================{}'.format(green, reset))
        print(' {}Valor em conta: {}{}{}'.format(yellow, green, ((30 - len(conta)) * ' ' + conta), reset ))
        print('{}================================================{}'.format(green, reset))
        print('')
    mov()
    dep_v =  str(input(' {}Entre com o valor do saque:\n\n {}~/{}Terminal{} $ '.format(blue, green, yellow, reset)))
    dep_v = rs.del_caracter(dep_v)
    mov()
    print(' {}Valor a sacar:  {}{}{}'.format(yellow, green, ((30 - len(dep_v)) * ' ' + dep_v), reset ))
    print('')
    dep_c = str(input(' {}Entre com a descrição do saque:\n\n {}~/{}Terminal{} $ '.format(blue, green, yellow, reset)))
    if dep_c == '' or dep_c == ' ' or dep_c == None:
        dep_c = 'valor aleatório'
    dep_c = dep_c.capitalize()
    print('')
    mov()
    print(' {}Valor a sacar:  {}{}{}'.format(yellow, green, ((30 - len(dep_v)) * ' ' + dep_v), reset ))
    print('')
    print(' {}Desc: {}{}{}'.format(yellow, cyan, dep_c, reset))
    conta_n = rs.float_to_s(rs.string_to_f(conta) - rs.string_to_f(dep_v))
    print('')
    print('{}================================================{}'.format(green, reset))
    print(' {}Valor após a movimentação:{}{}{}'.format(yellow, green, ((20 - len(conta_n)) * ' ' + conta_n), reset ))
    print('{}================================================{}'.format(green, reset))
    print('')
    print(' {}01{}]    {}Confirmar'.format(blue,reset, yellow))
    print(' {}02{}]    {}Corrigir'.format(blue,reset, yellow))
    print(' {}03{}]    {}Voltar'.format(blue,reset, yellow))
    print(' {}00{}]    {}Sair'.format(blue,reset, yellow))
    print('')
    rsp =  str(input(' {}Entre com o numero da opção:\n\n {}~/{}Terminal{} $ '.format(blue, green, yellow, reset)))
    if rsp == '00':
        os.system(os_cls)
    elif rsp == '01':
        os.system(os_cls)
        data = datetime.today().strftime('%d/%m/%Y')
        dep_v = rs.string_to_f(dep_v)
        dep_v = (dep_v - (2 * dep_v))
        dep_c = dep_c.lower()
        Control_DB.mov_func(data, 'saque', dep_v, dep_c, user)
        os.system('python {}App_CLI.py {} {}'.format(path_main, user, passwd))
    
    elif rsp == '02':
        os.system(os_cls)
        saque()
    elif rsp == '03':
        os.system(os_cls)
        menu_conta()
    else:
        os.system(os_cls)
        f_extrato(extrato)

def deposito():
    def mov():
        os.system(os_cls)
        print('{}================================================{}'.format(green, reset))
        print('               {}CAIXA DE ECONOMIAS{}            '.format(blue, reset))
        print('{}================================================{}'.format(green, reset))
        print(' {}Usuário: {}{}{}'.format(yellow, cyan, user, reset))
        print('{}================================================{}'.format(green, reset))
        print('{}------------------------------------------------{}'.format(magenta,reset))
        print('{} Deposito em conta {}'.format(yellow, reset))
        print('{}------------------------------------------------{}'.format(magenta, reset))
        print('{}================================================{}'.format(green, reset))
        print(' {}Valor em conta: {}{}{}'.format(yellow, green, ((30 - len(conta)) * ' ' + conta), reset ))
        print('{}================================================{}'.format(green, reset))
        print('')
    mov()
    dep_v =  str(input(' {}Entre com o valor do deposito:\n\n {}~/{}Terminal{} $ '.format(blue, green, yellow, reset)))
    dep_v = rs.del_caracter(dep_v)
    mov()
    print(' {}Valor a depositar:  {}{}{}'.format(yellow, green, ((26 - len(dep_v)) * ' ' + dep_v), reset ))
    print('')
    dep_c = str(input(' {}Entre com a descrição do deposito:\n\n {}~/{}Terminal{} $ '.format(blue, green, yellow, reset)))
    if dep_c == '' or dep_c == ' ' or dep_c == None:
        dep_c = 'valor aleatório'
    dep_c = dep_c.capitalize()
    print('')
    mov()
    print(' {}Valor a depositar:  {}{}{}'.format(yellow, green, ((26 - len(dep_v)) * ' ' + dep_v), reset ))
    print('')
    print(' {}Desc: {}{}{}'.format(yellow, cyan, dep_c, reset))
    conta_n = rs.float_to_s(rs.string_to_f(conta) + rs.string_to_f(dep_v))
    print('')
    print('{}================================================{}'.format(green, reset))
    print(' {}Valor após a movimentação:{}{}{}'.format(yellow, green, ((20 - len(conta_n)) * ' ' + conta_n), reset ))
    print('{}================================================{}'.format(green, reset))
    print('')
    print(' {}01{}]    {}Confirmar'.format(blue,reset, yellow))
    print(' {}02{}]    {}Corrigir'.format(blue,reset, yellow))
    print(' {}03{}]    {}Voltar'.format(blue,reset, yellow))
    print(' {}00{}]    {}Sair'.format(blue,reset, yellow))
    print('')
    rsp =  str(input(' {}Entre com o numero da opção:\n\n {}~/{}Terminal{} $ '.format(blue, green, yellow, reset)))
    if rsp == '00':
        os.system(os_cls)
    elif rsp == '01':
        os.system(os_cls)
        data = datetime.today().strftime('%d/%m/%Y')
        dep_v = rs.string_to_f(dep_v)
        dep_c = dep_c.lower()
        Control_DB.mov_func(data, 'deposito', dep_v, dep_c, user)
        os.system('python {}App_CLI.py {} {}'.format(path_main, user, passwd))
    
    elif rsp == '02':
        os.system(os_cls)
        deposito()
    elif rsp == '03':
        os.system(os_cls)
        menu_conta()
    else:
        os.system(os_cls)
        f_extrato(extrato)

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
        if i[1] == 'deposito' or i[1] == 'abertura':
            sp = ''
        else:
            sp = '   '
        print(' {}|{}{}{}| |{}{}{}| {}{}{}{}'.format(magenta, blue, i[1], magenta, blue, i[0], magenta, sp,green, ((22 - len(v_ex)) * ' ' + v_ex), reset))
        print('')
        print(' {}Desc: {}{}{}'.format(yellow, cyan, i[3].capitalize(), reset))
        print('{}------------------------------------------------{}'.format(magenta, reset))
    print('{}================================================{}'.format(green, reset))
    print(' {}Valor em conta: {}{}{}'.format(yellow, green, ((30 - len(conta)) * ' ' + conta), reset ))
    print('{}================================================{}'.format(green, reset))
    print('')
    print(' {}01{}]    {}Voltar'.format(blue,reset, yellow))
    print(' {}00{}]    {}Sair'.format(blue,reset, yellow))
    print('')
    print('{}================================================{}'.format(green, reset))
    print('')
    rsp = str(input(' {}Entre com o numero da opção:\n\n {}~/{}Terminal{} $ '.format(blue, green, yellow, reset)))
    
    if rsp == '00':
        os.system(os_cls)
    elif rsp == '01':
        os.system(os_cls)
        menu_conta()
    else:
        os.system(os_cls)
        f_extrato(extrato)

def menu_conta():
    os.system(os_cls)
    if tipo == 'deposito' or tipo == 'abertura':
        sp = ''
    else:
        sp = '   '
    print('{}================================================{}'.format(green, reset))
    print('               {}CAIXA DE ECONOMIAS{}            '.format(blue, reset))
    print('{}================================================{}'.format(green, reset))
    print(' {}Usuário: {}{}{}'.format(yellow, cyan, user, reset))
    print('{}================================================{}'.format(green, reset))
    print('{}------------------------------------------------{}'.format(magenta,reset))
    print(' {}DATA: {}{}                {}HORA: {}{}{}'.format(yellow, cyan, datetime.today().strftime('%d/%m/%Y'), yellow, cyan, datetime.today().strftime('%H:%M:%S'), reset))
    print('{}------------------------------------------------{}'.format(magenta,reset))
    print(' {}UltM: {}|{}{}{}| |{}{}{}| {}{}{}{}'.format(yellow , magenta, blue, tipo, magenta, blue, ultdata, magenta , sp, green, ((16 - len(ultvalor)) * ' ' + ultvalor), reset))
    print('{}------------------------------------------------{}'.format(magenta,reset))
    print('{}================================================{}'.format(green, reset))
    print(' {}Valor em conta: {}{}{}'.format(yellow, green, ((30 - len(conta)) * ' ' + conta), reset ))
    print('{}================================================{}'.format(green, reset))
    print('')
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
        deposito()
    elif rsp == '02':
        os.system(os_cls)
        saque()
    elif rsp == '03':
        os.system(os_cls)
        f_extrato(extrato)
    elif rsp == '04':
        os.system(os_cls)
        delete()
    else:
        menu_conta()

if __name__ == ('__main__'):
	menu_conta()
