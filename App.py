import os, sqlite3
from flask import Flask, render_template
from module.realsymbol import Real as rs
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def homepage():
	def ver():
		if os.path.isfile('settings/cde.db'):
			pass
		else:
			con = sqlite3.connect('settings/cde.db')
			cur = con.cursor()
			cur.execute('''CREATE TABLE movimentacao(Data date, TMov text, VMov real)''')
			cur.execute('''INSERT INTO movimentacao VALUES('{}', '{}', '{}')'''.format(datetime.today().strftime('%d/%m/%Y'), 'abertura', '0.0'))
			con.commit()
			con.close()
	def ultrow():
		con = sqlite3.connect('settings/cde.db')
		cur = con.cursor()
		for row in cur.execute('''SELECT * FROM movimentacao'''):
			ult = row
		x = ult[2]
		y = ult[1]
		z = ult[0]
		con.commit()
		con.close()
		return x, y, z
	def v_conta():
		ver()
		def del_car(x):
			x = x[0]
			if x == None:
				x = 0.0
			else:
				x = float(x)
			return x
		con = sqlite3.connect('settings/cde.db')
		cur = con.cursor()
		for row in cur.execute('''SELECT SUM(VMov) FROM movimentacao WHERE TMov='deposito' '''):
			deposito = row
			deposito = del_car(deposito)
		for row in cur.execute('''SELECT SUM(VMov) FROM movimentacao WHERE TMov='saque' '''):
			saque = row
		saque = del_car(saque)
		con.commit()
		con.close()
		return (deposito - saque)
	
	conta = rs.float_to_s(v_conta())
	ultC , ultO, dt = ultrow()
	ultC = rs.float_to_s(ultC)
	ultO = ultO.capitalize()
	return render_template('index.html', ultC = ultC, ultO = ultO, dt = dt, conta =  conta)

if __name__ == '__main__':
	app.run(debug=True)