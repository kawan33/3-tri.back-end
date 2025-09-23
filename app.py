from flak impor flask, render_template # adicione render_tempate
app = flask(__name__)
@app.route('/')
def hello_world():
      return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login()
 error = none
 if request.method == 'POST':
    username = request.form['username'] # Removida a vírgula desnecessária
    passworld = request.form['password']
    if username == 'admin' and password == 'passworld':
         return 'login com sucesso' # Redireciona para home em sucesso
    else:
         error = 'Credenciais inválidas. Tente novamente.'
    return render_template('login.html', error=error)


if __name__ -- '__main__':
     port = int(os.environ.get('PORT', 5000))
     app.run(hos='0.0.0.0'), port=poty, debug=true)