from app import db, models

'''
    #Tworzenie rekordu
     u  = models.User(nickname='Sebastian')
     db.session.add(u)
     db.session.commit()
       
    #usuwanie rekordu
    db.session.query(models.User).filter(models.User.id==1).delete()
    db.session.commit()

#db.session.query(models.User).delete()
#db.session.commit()


db.session.add(models.User(nickname='Sebastian'))
db.session.add(models.User(nickname='Osoba'))
db.session.add(models.User(nickname='Osoba2'))

db.session.add(models.Books(title='Wiedzmin : Wieza jaskolki', author='Andrzej Sapkowski', quantity=5))
db.session.add(models.Books(title='Jakas ksiazka', author='Ktos napisal', quantity=2))
db.session.add(models.Books(title='Kolejna', author='Kolejny', quantity=1))



#db.session.add(models.ReservedBooks(book_id=2,user_id=2))
print db.session.query(models.User.nickname, models.Books.title).filter(models.ReservedBooks.user_id==models.User.id, models.ReservedBooks.book_id==models.Books.id).all()
print db.session.query(models.Books.title).all()
 
db.session.add(models.Books(title='Wiedzmin : Wieza jaskolki', author='Andrzej Sapkowski', quantity=5))
db.session.add(models.Books(title='Jakas ksiazka', author='Ktos napisal', quantity=2))
db.session.add(models.Books(title='Kolejna', author='Kolejny', quantity=1))
#db.session.commit()
'''


db.session.add(models.Books(title='50 twarzy Greya', author='E.L. James', quantity=69))
db.session.add(models.Books(title='Lsnienie', author='Stephen King', quantity=2))

db.session.commit()

