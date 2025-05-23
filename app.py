from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/') # Rota inicial
def inicio():
    return render_template('index.html')








# Inicia a aplicação
if __name__ == '__main__':
    app.run(debug=True)
