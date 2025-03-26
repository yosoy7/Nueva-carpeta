from flask import Flask, render_template, request, redirect, url_for, session
from auth.registration import Registration
from auth.login import Login

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta_aqui'  # Cambia esto por una clave segura

registration = Registration()
login = Login()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login_route():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if login.authenticate(username, password):
            session['username'] = username
            return redirect(url_for('welcome'))
        else:
            return 'Usuario o contraseña incorrectos'
    
    return render_template('login.html')

@app.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        
        if registration.register_user(username, email, password):
            return redirect(url_for('login_route'))
        else:
            return 'Error: El usuario o email ya existe'
    
    return render_template('register.html')

@app.route('/welcome')
def welcome():
    if 'username' not in session:
        return redirect(url_for('login_route'))
    return render_template('welcome.html', username=session['username'])

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)