from librarysystem import db, models
from sqlalchemy.sql import and_

'''
    #Tworzenie rekordu
     u  = models.User(nickname='Sebastian')
     db.session.add(u)
     db.session.commit()
       
    #usuwanie rekordu
    db.session.query(models.User).filter(models.User.id==1).delete()
    db.session.commit()

    #usuwanie wszystkich
    db.session.query(models.User).delete()
    db.session.query(models.Books).delete()
    db.session.query(models.ReservedBooks).delete()
    db.session.commit()

#db.session.query(models.User).delete()
#db.session.commit()


db.session.add(models.User(nickname='Sebastian'))
db.session.add(models.User(nickname='Osoba'))
db.session.add(models.User(nickname='Osoba2'))

db.session.add(models.Books(title='Wiedzmin : Wieza jaskolki', author='Andrzej Sapkowski', quantity=5))
db.session.add(models.Books(title='Jakas ksiazka', author='Ktos napisal', quantity=2))
db.session.add(models.Books(title='Kolejna', author='Kolejny', quantity=1))
db.session.add(models.Books(title='Wiedzmin : Wieza jaskolki', author='Andrzej Sapkowski', quantity=5))
db.session.add(models.Books(title='Jakas ksiazka', author='Ktos napisal', quantity=2))
db.session.add(models.Books(title='Kolejna', author='Kolejny', quantity=1))
db.session.add(models.Books(title='50 twarzy Greya', author='E.L. James', quantity=69))
db.session.add(models.Books(title='Lsnienie', author='Stephen King', quantity=2))

#db.session.add(models.ReservedBooks(book_id=2,user_id=2))
print db.session.query(models.User.nickname, models.Books.title).filter(models.ReservedBooks.user_id==models.User.id, models.ReservedBooks.book_id==models.Books.id).all()
print db.session.query(models.Books.title).all()


#db.session.commit()



print 'Uzytkownikcy: '
rec = db.session.query(models.User).all()
for record in rec:
    print record.nickname, ' ', record.id
dbUser = db.session.query(models.User.nickname, models.User.id).filter(models.User.nickname == 'Sebastian').all()
for dbu in dbUser:
    print dbu.id

print 'Ksiazki: '
books = db.session.query(models.Books).all()
for book in books:
    print book.id, ' ', book.title

print 'Zarezerowowane ksiazki:'
reserved = db.session.query(models.ReservedBooks).all()
for res in reserved:
    print res.user_id, ' ', res.book_id

print 'Wypozyczone przez Sebastian'
records= db.session.query(models.User.nickname, models.Books).join(models.ReservedBooks, models.Books).filter(models.User.id==dbUser[0].id).all()
print records
for rec in records:
    print rec[0], ' ', rec[1].title


db.session.commit()
db.session.add(models.User(nickname='Sebastian',password='sebastian'))
db.session.commit()


'''
#q=db.session.query(models.Books).filter(models.Books.id==1)
#q.one().quantity-=1
#db.session.commit()
 
record = db.session.query(models.User.nickname).all()
for rec in record:
    print rec.nickname

#print db.session.query(models.ReservedBooks).all()


