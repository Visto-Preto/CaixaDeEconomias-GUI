#!/data/data/com.termux/files/usr/bin/env python3

import sys, os

def platform():
	if sys.platform == 'linux':
		if os.path.isdir('/data/data/com.termux/files/usr/share/cde/'):
			path_main = '/data/data/com.termux/files/usr/share/cde/'
			path_db = '/data/data/com.termux/files/usr/share/cde/settings/'
		
		os_cls = 'clear'
		red = '\033[1;31m'
		green = '\033[1;32m'
		yellow = '\033[1;33m'
		blue = '\033[1;34m'
		magenta = '\033[1;35m'
		cyan = '\033[1;36m'
		reset = '\033[m'


	elif sys.platform == 'win32':	
		path_main = ''
		path_db = 'settings/'
		
		os_cls = 'cls'
		red = ''
		green = ''
		yellow = ''
		blue = ''
		magenta = ''
		cyan = ''
		reset = ''
	else:
		print('Sistema operacional nao suportado')
