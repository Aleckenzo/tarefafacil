# TarefaFácil — Aplicação web simples para gerenciamento de tarefas

Aplicação web para gerenciar tarefas, construída com Python e Flask, com uma interface simples em HTML e CSS utilizando templates Jinja2 para renderização dinâmica.

---

## 📌 Visão Geral

TarefaFácil é um app para criar, listar, concluir e remover tarefas do dia a dia. Ideal para quem quer uma lista de tarefas simples, rápida e acessível pelo navegador.

---

## 🔍 Funcionalidades

✅ Adicionar novas tarefas com descrição

✅ Listar todas as tarefas pendentes e concluídas

✅ Marcar tarefas como concluídas

✅ Remover tarefas da lista

✅ Atualização dinâmica da lista com redirecionamentos simples

---

## 🧱 Tecnologias Utilizadas

### 🖥️ Backend

- Python
- Flask (microframework web)

### 💻 Frontend

- HTML
- CSS
- Jinja2 (motor de templates do Flask)

---

## 🧠 Arquitetura do Projeto

```
tarefafacil/
├── app.py                  # Código principal da aplicação Flask
├── templates/
│   └── index.html          # Template HTML com Jinja2 para a interface
├── static/
│   └── style.css           # Arquivo CSS para estilização da página
├── README.md               # Documentação do projeto
└── requirements.txt        # Dependências Python
```

---

## 🚀 Como Rodar o Projeto

1. Clone o repositório:

```bash
git clone https://github.com/Aleckenzo/tarefafacil.git
cd tarefafacil
```

2. Crie e ative um ambiente virtual:

- No Linux/Mac:

```bash
python3 -m venv venv
source venv/bin/activate
```

- No Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Execute a aplicação:

```bash
python app.py
```

5. Acesse no navegador:

[http://127.0.0.1:5000/](http://127.0.0.1:5000/)

---

## ⚙️ Fluxo da Aplicação

- O backend Flask recebe as requisições e manipula a lista de tarefas armazenada em memória.

- O template Jinja2 gera o HTML dinamicamente, exibindo as tarefas e os botões para concluir ou remover.

- Formulário para adicionar novas tarefas envia dados via POST para o backend.

- Cada tarefa tem um índice que é usado nas rotas para concluir ou remover.

---

Feito com ❤️ para ajudar a organizar seu dia com simplicidade!




