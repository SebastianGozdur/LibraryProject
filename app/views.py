from flask import render_template, redirect, url_for, request, flash
from app import app
from app import db, models




@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',title='Something',user='Example')

class UserVariable: 
    user = ' '



@app.route('/login', methods=['POST'])
def login():
    if 'login' in request.form:
        UserVariable.user = request.form['nickname'] 
    else:
        ids=request.form['id']
        idList=ids.split(',')
        flash('Reserved books: "%s"' % (ids))
        allBooks = db.session.query(models.Books).all()
        for book in idList:
            if findBook(book, allBooks) == False:
                flash('Nie istnieje ksiazka o id "%s"' % book)       

    dbUser = db.session.query(models.User.nickname, models.User.id).filter(models.User.nickname == UserVariable.user).all()
    if UserVariable.user == dbUser[0].nickname:   
        reservedBooks=db.session.query(models.User.nickname, models.Books).join(models.ReservedBooks, models.Books).filter(models.User.id==dbUser[0].id).all()
        availableBooks=db.session.query(models.Books).all()
        return render_template('login.html', title='Log In', name=UserVariable.user, reservedBooks=reservedBooks, availableBooks=availableBooks)


def findBook(bookId, records):
    for rec in records:
        if rec.id == bookId:
            return True
    return False







