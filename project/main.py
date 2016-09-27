#!/usr/bin/env python
## -*- coding: utf-8 -*-
from flask import Flask
from flask import render_template
from flask import request, make_response
from flask import session, flash
from flask import redirect, url_for
from flask_wtf import CsrfProtect
import forms

app = Flask(__name__)
app.secret_key = 'my_secret_key'
csrf = CsrfProtect(app)

@app.route('/')
def index():
    if 'username' in session:
        username = session['username']
        print username

    title = 'Index'
    return render_template('index.html', title = title)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    login_form = forms.LoginForm(request.form)
    if request.method == 'POST' and login_form.validate():
        username = login_form.username.data
        success_message = 'Bienvenido {}'.format(username)
        flash(success_message)
        session['username'] = login_form.username.data
        
    return render_template('login.html', form = login_form)

@app.route('/logout')
def logout():
    if 'username' in session:
        session.pop('username')
    return redirect(url_for('login'))

@app.route('/cookie')
def cookie():
    response = make_response(render_template('cookie.html'))
    response.set_cookie('custome_cookie', 'Sebastian')
    return response

@app.route('/comment', methods = ['GET', 'POST'])
def comment():
    comment_form = forms.CommentForm(request.form)

    if request.method == 'POST' and comment_form.validate():
        print comment_form.username.data
        print comment_form.email.data
        print comment_form.comment.data
    else:
        print 'Error en el formulario'

    title = "Curso Flask"
    return render_template('comment.html', title = title, form = comment_form)

if __name__ == '__main__':
    app.run(debug = True, port = 8000)
