from flask import Flask,render_template,request, flash, redirect, url_for, session, logging
app = Flask(__name__)
app.secret_key = 'some secret key'

@app.route('/')
def index():
 	return render_template('index.html')


if __name__=='__main__':
	app.secret_key = 'some secret key'
	#ebug(True)
	app.run(debug = True)
