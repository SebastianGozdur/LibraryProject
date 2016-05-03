from librarysystem import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(64))
    password = db.Column(db.String(64))

    def getId(self):
        return self.id

    def getNickname(self):
        return self.nickname

class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    author = db.Column(db.String(120))
    quantity = db.Column(db.Integer)

    def getTitle(self):
        return self.title

    def getAuthor(self):
        return self.author

    def getQuantity(self):
        return self.quantity


class ReservedBooks(db.Model):  
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    book_id = db.Column(db.Integer, db.ForeignKey('books.id'))

    def getUserId(self):
        return self.user_id

    def getBookId(self):
        return self.book_id

