from flask import Flask,render_template,request
import urllib.request,json

app = Flask(__name__)

pessoas = []
@app.route('/primeiro',methods=['GET','POST'])
def principal():
    if request.method == 'POST':
        if request.form.get("aluno"):                           #verifica se aluno foi preenchido 
            pessoas.append(request.form.get("aluno"))           #maneira de acessar dados enviados por um formulário HTML em uma solicitação POST.
    return render_template ("principal.html", pessoas=pessoas)


registro = []
@app.route('/sobre',methods=['GET','POST'])
def sobre():
    if request.method == 'POST':
        if request.form.get('pessoa') and request.form.get("idade"):
            registro.append({'pessoa': request.form.get ("pessoa"),'idade': request.form.get('idade')})
    return render_template('sobre.html', registro = registro)


@app.route('/filmes', methods=['GET','POST'])
def filmes():
    url = 'https://api.themoviedb.org/3/discover/movie?sort_by=popularity.desc&api_key=a6acfd71bbff6e08ae7bda668ede33c5'
    resposta = urllib.request.urlopen(url)
    dados = resposta.read()
    jsondata = json.loads(dados)
    return render_template ('filmes.html', filmes=jsondata['results'])


@app.route('/', methods=['GET','POST'])
def inicio():
    return render_template ('inicio.html')


if __name__ == "__main__":
    app.run(debug=True)