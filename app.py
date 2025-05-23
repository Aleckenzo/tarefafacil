from flask import Flask, render_template, request, redirect

app = Flask(__name__)

listaTarefas = []

@app.route('/') # Rota inicial
def inicio():
    return render_template('index.html', tarefas = listaTarefas)

@app.route('/adicionar', methods=['POST'])
def adicionar():
    descricao = request.form['descricao']  # Pega o valor do campo 'descricao' enviado pelo formulário
    if descricao: # verifica se o valor da variável descricao não está vazio. # é o equivalente de: if descricao != '' and descricao is not None:
        listaTarefas.append({'descricao': descricao, 'concluida': False})
    return redirect('/')

@app.route('/concluir/<int:id_tarefa>')
def concluir(id_tarefa):
    listaTarefas[id_tarefa]['concluida'] = True
    return redirect('/')

@app.route('/remover/<int:id_tarefa>')
def remover(id_tarefa):
    listaTarefas.pop(id_tarefa)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
