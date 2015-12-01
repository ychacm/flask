from app import app
from flask import render_template,flash,redirect
from .forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',title='Home')


@app.route('/login',methods=['GET','POST'])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        flash('Login requested fro OpendID="'+ form.openid.data +'",remember_me='+str(form.remember_me.data))
        return redirect('/index')
    return render_template('login.html',title='Sign in',form=form)
