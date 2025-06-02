#!/usr/bin/python3

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(os.path.dirname(__file__), 'todoApp.db')
db = SQLAlchemy(app)


@app.route('/')
def index():
    todoAll = Todo.query.all()
    return render_template('index.html', todoAll=todoAll)


@app.route('/ekle', methods=['POST'])
def ekle():
    title = request.form.get('title')
    content = request.form.get('content')

    newTodo = Todo(title=title, content=content, status=False)
    db.session.add(newTodo)
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/status/<string:id>')
def durum(id):
    todo = Todo.query.filter_by(id=id).first()
    if (todo.status is False):
        todo.status = True
    else:
        todo.status = False

    db.session.commit()
    return redirect(url_for('index'))


@app.route('/delete/<string:id>')
def sil(id):
    todo = Todo.query.filter_by(id=id).first()
    db.session.delete(todo)
    db.session.commit()

    return redirect(url_for('index'))


@app.route('/details/<string:id>')
def detaylar(id):
    todo = Todo.query.filter_by(id=id).first()
    todoAll = Todo.query.all()

    if todo in todoAll:
        return render_template('details.html', todo=todo)
    else:
        return redirect(url_for('index'))


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    content = db.Column(db.Text)
    status = db.Column(db.Boolean)


if __name__ == '__main__':
    app.run(debug=True)
