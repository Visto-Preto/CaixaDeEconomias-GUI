#!/data/data/com.termux/files/usr/bin/env python3
import os, sys, getpass, time, sqlite3
from datetime import datetime

#coding: utf8


red = '\033[1;31m'
green = '\033[1;32m'
yellow = '\033[1;33m'
blue = '\033[1;34m'
magenta = '\033[1;35m'
cyan = '\033[1;36m'
cls = '\033[m'


def menu_users():
	os.system('clear')
	menu = '''
{}================================================
               {}CAIXA DE ECONOMIAS           
{}================================================
{}------------------------------------------------
{}Usuarios cadrastados
{}------------------------------------------------{}
'''.format( green, 
            blue, 
            green, 
            magenta, 
            yellow,
            magenta,
            cyan)

	print(menu)
	users = os.listdir('settings')
	for i in (users):
		print(i[:-3])

	menu_b = '''
{}------------------------------------------------	
{}================================================
'''.format(magenta,
            green,
            cls)
	print(menu_b)

def menu_users_none(x):
	os.system('clear')
	menu = '''
{}================================================
               {}CAIXA DE ECONOMIAS           
{}================================================
{}------------------------------------------------
{}O usuario {}{}{} não esta cadrastados
{}------------------------------------------------
{}================================================{}
'''.format( green, 
            blue, 
            green, 
            magenta, 
            yellow,
            cyan,
            x,
            yellow, 
            magenta, 
            green,
            cls)
	print(menu)


def menu_users_login(user):
	con = sqlite3.connect('settings/' + user + '.db')
	cur = con.cursor()
	for pswd_db in cur.execute('''SELECT pswd FROM dados_login'''):
		pswd_db = pswd_db[0]
		print(pswd_db)

	os.system('clear')
	menu = '''
{}================================================
               {}CAIXA DE ECONOMIAS           
{}================================================
{}------------------------------------------------
{}Usuário: {}{}
{}------------------------------------------------
{}================================================{}
'''.format( green, 
            blue, 
            green, 
            magenta, 
            yellow,
            cyan,
            user,
            magenta, 
            green,
            cls)
	print(menu)
	rsp = str(getpass.getpass('{}Entre com o password:\n\n{}~/{}Terminal{} $ '.format(blue, green, yellow, cls)))
	if rsp == pswd_db:
		os.system('python App_ClI.py {} {}'.format(user, pswd_db))
	else:
		os.system('clear')
		print('{}senha incorreta.{}'.format(red, cls))
		time.sleep(0.5)




def menu_conta(x, y, z):
    menu = '''
{}================================================
               {}CAIXA DE ECONOMIAS           
{}================================================
{}Usuário: {}{}
{}================================================
{}------------------------------------------------
{}DATA: {}{}                {}HORA: {}{}
{}------------------------------------------------
{}UltM: {}|{}{}{}| |{}{}{}|{} {}{}
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
    os.system('clear')
    print(menu)
    print(x())