import os, sqlite3
from flask import Flask, render_template, url_for, redirect, request, session
from module.realsymbol import Real as rs
from datetime import datetime

__author__ = "Visto-Preto"
__version__ = "1.0.0"

app = Flask(__name__)
app.secret_key = "evppdepf"

class Control_DB():
	def ver():
		if os.path.isfile('settings/cde.db'):
			pass
		else:
			con = sqlite3.connect('settings/cde.db')
			cur = con.cursor()
			cur.execute('''CREATE TABLE movimentacao(Data date, TMov text, VMov real)''')
			cur.execute('''INSERT INTO movimentacao VALUES('{}', '{}', '{}', '{}')'''.format(datetime.today().strftime('%d/%m/%Y'), 'abertura', '0.0', 'abertura da conta do caixa de economias'))
			con.commit()
			con.close()

	def ultrow():
		Control_DB.ver()
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
		Control_DB.ver()
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

	def mov_func(x,y,z,a):
		con = sqlite3.connect('settings/cde.db')
		cur = con.cursor()
		cur.execute('''INSERT INTO movimentacao VALUES('{}', '{}', '{}', '{}')'''.format(x, y, z, a))
		con.commit()
		con.close()

@app.route('/')
def login():
	if ( session ):
		return redirect( url_for('homepage') )
	else:
		return render_template('login.html')

@app.route('/action_page', methods=["POST"])
def action_page():
	if request.form['user'] == 'vp230' and request.form['pswd'] == '123456':
		session['usuario'] = request.form['user']

		return redirect( url_for('homepage') )
	return redirect( url_for('login') )

@app.route('/cadastro')
def cadastro():
	return render_template('cadastro.html')

@app.route('/action_cadastro', methods=["POST"])
def action_cadastro():
	user =  request.form["user"]
	pswd =  request.form["pswd"]
	email =  request.form["email"]

	def ver(x,y,z):
		if os.path.isfile('settings/' + user + '.db'):
			pass
		else:
			con = sqlite3.connect('settings/' + user + '.db')
			cur = con.cursor()
			cur.execute('''CREATE TABLE dados_login(uname TEXT, pswd TEXT, email TEXT)''')
			cur.execute('''INSERT INTO dados_login VALUES('{}', '{}', '{}')'''.format(x, y, z))
			cur.execute('''CREATE TABLE movimentacao(Data DATE, TMov TEXT, VMov REAL, Descricao TEXT)''')			
			cur.execute('''INSERT INTO movimentacao VALUES('{}', '{}', '{}', '{}')'''.format(datetime.today().strftime('%d/%m/%Y'), 'abertura', '0.0', 'abertura da conta do caixa de economias'))
			con.commit()
			con.close()

	ver(user, pswd, email)
	
	return 'email: {}<br>user: {}<br>pass: {}'.format(email, user, pswd)

@app.route('/homepage')
def homepage():
	if (session):
		ultC , ultO, dt, li = Control_DB.ultrow()
		if ultC > 0:
			cor_ultC = '#00CC00'
		elif ultC  < 0:
			cor_ultC = '#DF0101'
		else:
			cor_ultC = '#33CCFF'
		conta = rs.float_to_s(Control_DB.v_conta())
		cor_conta = rs.string_to_f(conta)
		if cor_conta > 0:
			cor_conta = '#00CC00'
		elif cor_conta < 0:
			cor_conta = '#DF0101'
		else:
			cor_conta = '#33CCFF'
		ultC = rs.float_to_s(ultC)
		ultO = ultO.capitalize()
		return render_template('index.html', ultC = ultC, cor_ultC = cor_ultC, ultO = ultO, dt = dt, conta =  conta, cor_conta = cor_conta, real = rs.float_to_s)
	else:
		return redirect( url_for('login') )

@app.route('/extratos')
def extratos():
	if ( session ):
		Control_DB.ver()
		a, b, c, li = Control_DB.ultrow()
		li = li[::-1]
		return render_template('extratos.html', li = li, real = rs.float_to_s)
	return redirect( url_for('login') )

@app.route('/movimentacao', methods=["POST"])
def movimentacao():
	tipo =  request.form["tipo"]
	movto =  request.form["movimento"]
	desc =  request.form["desc"]
	if desc == '':
		desc = 'valor aleatório'
	desc = desc.lower()
	if movto == '':
		movto = 0
	if tipo == 'saque':
		movto = (float(movto) - (2 * float(movto)))
	data = datetime.today().strftime('%d/%m/%Y')
	Control_DB.mov_func(data, tipo, movto, desc)
	return redirect( url_for('homepage') )

@app.route('/sair')
def sair():
	session.pop('usuario', None)
	return redirect( url_for('login') )

if __name__ == '__main__':
	app.run(debug=True, host="0.0.0.0")