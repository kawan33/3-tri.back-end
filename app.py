# rodar no cmd
#pip install flash 
#importar a biblioteca flash
from flash import flask 
#cria uma isntância da aplicação flask
app= flask(__name__)
# Este é um decorar que associa a URL
# '/' (a URL raiz do site) à função que vem logo abaixo.
@app.route('/')
# A função que é e executada quando a rota '/' é acessada. 
# Ela retorna a string "Hello, World!".
def hello_world()
    return 'hello, world!'

    #executar o servidor de desesnvolvimeto 
    if __name__ == '__main__':
        app.run(debug=true)