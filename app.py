from flask import Flask, render_template  # Adicione render_template
app = Flask(__name__)
@app.route('/')
def hello_world():
       return render_template('index.html')
       
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']  # Removida a vírgula desnecessária
        password = request.form['password']
        if username == 'admin' and password == 'password':
            return 'Login com sucesso'  # Redireciona para home em sucesso
        else:
            error = 'Credenciais inválidas. Tente novamente.'
    return render_template('login.html', error=error)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)


render.yaml

services:
  - type: web
    name: meu-flask-app
    env: python
    buildCommand: pip install -r requirements.txt
    startCommand: gunicorn app:app
    plan: free

requirements.txtFlask==3.0.3
gunicorn==22.0.0
templates /
index.html

<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>Meu App Flask</title>
</head>
<body>
    <h1>Hello, World!</h1>
    <p>Este é o meu primeiro site no Render!</p>
</body>
</html>

login.html

<!DOCTYPE html>
<html>
    <head>
        <title> Login </title>
    </head>
    <body>
        <main>
            <form method="POST" action="/login">
                <label for="username"> Username: </label>
                <input type="text" id="username" name="username" required>
                <br>
                <label for="password"> Password: </label>
                <input type="password" id="password" name="password" required>
                <br>
                <button type="submit"> Login </button>
    </body>
</html>
