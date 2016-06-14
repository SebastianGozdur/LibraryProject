from flask import render_template, redirect, request, flash
from librarysystem import app
from librarysystem import db, models
import base64

import sys

@app.route('/')
@app.route('/index')
def index():
    reload(sys)
    sys.setdefaultencoding('utf8')   #do polskich znakow
    return render_template('index.html',title='LibrarySystem')

class UserVariable:
    user = ' '
    password = ' '
    user_id = 0

@app.route('/login', methods=['POST'])
def login():
    if 'login' in request.form:
        UserVariable.user = request.form['nickname']
        UserVariable.password = request.form['password']
    elif 'remove' in request.form:
	   ids = request.form['id']
	   idList = ids.split(',') 
	   for book in idList:
		  try:
		    bood = int(book)
		  except:
		    flash('Zly format')
		    continue
		  userBooks = db.session.query(models.ReservedBooks).filter(models.ReservedBooks.user_id==UserVariable.user_id).all()
		  if findUserBook(book,userBooks)==True:
		      db.session.query(models.ReservedBooks).filter(models.ReservedBooks.user_id==UserVariable.user_id, models.ReservedBooks.book_id==book).delete()
		      db.session.query(models.Books).filter(models.Books.id==book).one().quantity+=1
		      db.session.commit()
		      flash('Ksiazka o id "%s" zostala usunieta' % book)
		  else:
		      flash('Nie ma ksiazki o id "%s" w Twoich rezerwacjach' % book)
	 
    else:
        ids=request.form['id']
        idList=ids.split(',')
        allBooks = db.session.query(models.Books).all()
	for book in idList:
	      try:
		bood = int(book)
	      except:
		 flash('Zly format')
		 continue
	      if findBook(book, allBooks) == False:
		flash('Nie istnieje ksiazka o id "%s"' % book)
	      elif isAlreadyBorrowed(book,UserVariable.user_id):
		flash('Ksiazka o id "%s" jest juz przez Ciebie wypozyczona' % book)
	      elif isAvailable(book):
		flash('Nie ma ksiazki o id "%s" na stanie. Sprobuj kiedy indziej' % book)
	      else:
		flash('Zarezerowowano ksiazki o id: "%s"' % book)
		db.session.add(models.ReservedBooks(book_id=book, user_id=UserVariable.user_id))
		db.session.commit()
	    
	    
    dbUser = db.session.query(models.User).filter(models.User.nickname == UserVariable.user).all()

    
    if len(dbUser) == 0:
        flash('Nie ma uzytkownika')
        return redirect('/index')
      
    currentPassword = dbUser[0].password
    currentPassword = base64.b64decode(currentPassword +"===") 
    if currentPassword != UserVariable.password:
        flash('Bledne haslo')
        return redirect('/index')
    if UserVariable.user == dbUser[0].nickname:
        UserVariable.user_id=dbUser[0].id
        reservedBooks=db.session.query(models.User.nickname, models.Books).join(models.ReservedBooks, models.Books).filter(models.User.id==dbUser[0].id).all()
        availableBooks=db.session.query(models.Books).all()
        return render_template('login.html', title='Logowanie', name=UserVariable.user, reservedBooks=reservedBooks, availableBooks=availableBooks)

def findBook(bookId, records):
    for rec in records:
        if int(rec.id) == int(bookId):
            return True
    return False

def findUserBook(bookId, records):
    for rec in records:
        if int(rec.book_id)== int(bookId):
            return True
    return False

def isAvailable(bookId):
    q=db.session.query(models.Books).filter(models.Books.id==bookId)
    if int(q.one().quantity) > 0:
        q.one().quantity-=1
        return False
    return True

def isAlreadyBorrowed(bookId,userId):
    record = db.session.query(models.ReservedBooks).filter(models.ReservedBooks.user_id == userId, models.ReservedBooks.book_id==bookId).all()
    if len(record) == 0:
        return False
    return True


@app.route('/registration', methods=['POST','GET'])
def registration():

    if 'register' in request.form:
        nickname = request.form['nickname']
        if isUserAvailable(nickname):
            password =  request.form['password']
            password = base64.b64encode(password)
            db.session.add(models.User(nickname=nickname,password=password))
            db.session.commit()
            flash('Konto zostalo utworzone')
        else:
        	flash('Konto o podanym loginie juz istnieje')
    return render_template('registration.html')


def isUserAvailable(username):
    record = db.session.query(models.User.nickname).filter(models.User.nickname == username).all()
    if len(record) == 0:
        return True
    return False



@app.route('/help')
def help():
	return render_template('help.html')
      

@app.route('/admin', methods=['POST'])
def admin():
    if 'admin' in request.form:
      adminUser = db.session.query(models.Administrators).filter(models.Administrators.nickname == request.form['nickname']).all()
      if len(adminUser) != 0:
	  if request.form['password'] == adminUser[0].password:
	      availableBooks=db.session.query(models.Books).all()
	      return render_template('admin.html', availableBooks=availableBooks)
      else:
	    flash('Nie ma uzytkownika')
	    return render_template('adminLogin.html')
    elif 'add' in request.form:
      title = request.form['title']
      author = request.form['author']
      quantity = request.form['quantity']
      db.session.add(models.Books(title=title, author=author, quantity=quantity))
      db.session.commit()
      availableBooks=db.session.query(models.Books).all()
      flash('Dodano wprowadzona ksiazke')
      return render_template('admin.html', availableBooks=availableBooks)
    elif 'delete' in request.form:
      bookId = request.form['id']
      db.session.query(models.Books).filter(models.Books.id==bookId).delete()
      db.session.query(models.ReservedBooks).filter(models.ReservedBooks.bookId == bookId).delete()
      db.session.commit()
      availableBooks=db.session.query(models.Books).all()
      flash('Usunieto wprowadzona ksiazke i rezerwacje')
      return render_template('admin.html', availableBooks=availableBooks)
      


@app.route('/adminlogin',methods=['GET'])
def adminlogin():
    return render_template('adminLogin.html')


