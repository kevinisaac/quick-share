from flask import Flask, render_template, request
import db_ops

app = Flask(__name__)

@app.route('/')
@app.route('/home')
@app.route('/index')

def home():
	return render_template('home.html')

#@app.route('/login')

#def login():

#	err = None
#	if request.method == 'POST':
@app.route('/signup')
def signup():
        return render_template('signup.html', error="Create a new Account")


@app.route('/signup_process', methods=['POST'])
def signup_process():
	if request.method == 'POST':
		state = db_ops.signup(request.form['uname'], request.form['passwd'])
		return render_template('signup.html', error=state)
	else:
		return render_template('signup.html', error="Create a new Account")
					


if __name__ == '__main__':
	app.run(debug=True)
