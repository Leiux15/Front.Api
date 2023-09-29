from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Simulando um banco de dados de usuários (substitua isso por um banco de dados real)
users = {'usuario1': 'senha1', 'usuario2': 'senha2'}

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if username in users and users[username] == password:
        # Autenticação bem-sucedida, redirecione para o painel.
        return redirect(url_for('dashboard'))
    else:
        # Autenticação mal-sucedida, exiba uma mensagem de erro.
        error_message = 'Credenciais inválidas. Tente novamente.'
        return render_template('login.html', error=error_message)

@app.route('/dashboard')
def dashboard():
    # Esta é a página principal do seu aplicativo após o login bem-sucedido.
    return 'Bem-vindo ao painel!'

if __name__ == '__main__':
    app.run(debug=True)
