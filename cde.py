#!/data/data/com.termux/files/usr/bin/env python3

import sys, os
from module import menus_cli
# ________________________________

__author__ = 'Visto-Preto'
__version__ = '1.0.0'

# ________________________________
# Paths

path_app_gui_t = '/data/data/com.termux/files/usr/share/cde/App.py'
path_app_gui = 'App.py'

path_app_cli_t = '/data/data/com.termux/files/usr/share/cde/App_CLI.py'
path_app_cli = 'App_CLI.py'


# ________________________________


arg1 = ''
arg2 = ''
arg3 = ''

if len(sys.argv) == 1: #0
	arg0 = ''
elif len(sys.argv) == 2: #1
	arg1 = sys.argv[1]

elif len(sys.argv) == 3: #2
	arg1 = sys.argv[1]
	arg2 = sys.argv[2]

elif len(sys.argv) == 4: #3
	arg1 = sys.argv[1]
	arg2 = sys.argv[2]
	arg3 = sys.argv[3]
else:
	arg = 'err'

descricao = '''

cde	[about] [start [-gui [-server]] [-cli [username] [-create]] [-list]]
	[uninstall] [upgrade]

about	Sobre o script
start -gui	Inciar GUI no browser
start -gui -server	Inciar servidor de GUI
start -cli [username]	Inciar o App em CLI
start -cli -create	Criar novo usuarios
start -list	Lista de usuarios cadrastrado
uninstall	Remover a instalação do script

'''

def arg_analise(x, y, z):
	if x == 'about':
		print()
		print('Desenvolvido por ', __author__)
		print('Version ', __version__)
		print()
	elif x == 'start' and y == '-gui' and z == '':
		os.system('bash /data/data/com.termux/files/usr/share/cde/gui.sh')
	elif x == 'start' and y == '-gui' and z == '-server':
		os.system('python {}'.format(path_app_gui))

	elif x == 'start' and y == '-cli' and z == '-create':
		print('criar usuarios')

	elif x == 'start' and y == '-cli' and z == '-list':
		menus_cli.menu_users()

	elif x == 'start' and y == '-cli' and z != '':
		if os.path.isfile('settings/' + z + '.db'):
			menus_cli.menu_users_login(z)
		else:
			menus_cli.menu_users_none(z)

		
	elif x == 'uninstall':
		os.system('bash /data/data/com.termux/files/usr/share/cde/uninstall.sh')
	else:
		print(descricao)

arg_analise(arg1, arg2, arg3)
