from flask import Flask, render_template, url_for, redirect, request
from flask_bootstrap import Bootstrap5

import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
Bootstrap5(app)


data_entries = [{'task':'Create a todo',
                 'done': False
                 },
                {
                    'task': 'Test',
                    'done': True
                }
                ]
@app.route("/")
def main():

    return render_template('index.html',)



@app.route("/todo")
def todo():
    return render_template('todo.html',data_entries=data_entries)

@app.route("/add", methods=['POST'])
def add():
    data = request.form['nm']
    data_entries.append({'task': data, 'done': False})
    return redirect(url_for('todo'))

@app.route('/check/<int:index>')
def check(index):
    data_entries[index]['done'] = not data_entries[index]['done']
    return redirect(url_for('todo'))

@app.route("/delete/<int:index>")
def delete(index):
         del data_entries[index]
         return redirect(url_for('todo'))


if __name__ == "__main__":
    app.run(debug=False)