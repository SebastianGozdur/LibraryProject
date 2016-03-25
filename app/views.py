from flask import render_template, flash, redirect
from app import app
from app import db, models
from .forms import LoginForm

@app.route('/')

@app.route('/login')
@app.route('/index', methods=['GET','POST'])
def index():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="%s", password=%s' % (form.openid.data, str(form.password.data)))
        print form.openid.data
        return redirect('/index')
    records=db.session.query(models.Books)
    return render_template('index.html',title='Library System',user='Sebastian', records=records, form=form)



                      
