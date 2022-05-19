import os, sqlite3
from flask import Flask, render_template, url_for, redirect, request
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
		ver()
		con = sqlite3.connect('settings/cde.db')
		cur = con.cursor()
		li = []
		for row in cur.execute('''SELECT * FROM movimentacao'''):
			ult = row
			li += [row]
		x = ult[2]
		y = ult[1]
		z = ult[0]

		con.commit()
		con.close()
		return x, y, z, li
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
		for row in cur.execute('''SELECT SUM(VMov) FROM movimentacao '''):
			conta = row
			conta = del_car(conta)
		con.commit()
		con.close()
		return conta
	
	ultC , ultO, dt, li = ultrow()
	if ultC > 0:
		cor_ultC = '#00CC00'
	elif ultC  < 0:
		cor_ultC = '#DF0101'
	else:
		cor_ultC = '#33CCFF'

	conta = rs.float_to_s(v_conta())
	cor_conta = rs.string_to_f(conta)
	if cor_conta > 0:
		cor_conta = '#00CC00'
	elif cor_conta < 0:
		cor_conta = '#DF0101'
	else:
		cor_conta = '#33CCFF'


	ultC = rs.float_to_s(ultC)
	ultO = ultO.capitalize()
	return render_template('index2.html', ultC = ultC, cor_ultC = cor_ultC, ultO = ultO, dt = dt, conta =  conta, cor_conta = cor_conta, li = li, real = rs.float_to_s)



@app.route('/movimentacao', methods=['GET'])
def movimentacao():
	tipo = request.args.get("tipo")
	movto = request.args.get("movimento")
	desc = request.args.get("desc")
	desc = desc.lower()
	if movto == '':
		movto = 0
	if tipo == 'saque':
		movto = (float(movto) - (2 * float(movto)))


	data = datetime.today().strftime('%d/%m/%Y')
	def mov_func(x,y,z,a):
		con = sqlite3.connect('settings/cde.db')
		cur = con.cursor()
		cur.execute('''INSERT INTO movimentacao VALUES('{}', '{}', '{}', '{}')'''.format(x, y, z, a))
		con.commit()
		con.close()
	mov_func(data, tipo, movto, desc)
	return redirect( url_for('homepage') )



if __name__ == '__main__':
	app.run(debug=True)