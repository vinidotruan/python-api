from bootstrap import app, db, jsonify

class Book(db.Model):
    __tablename__ = "books"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), unique=False, nullable=False)
    author = db.Column(db.String(255), unique=False, nullable=False)

    def __repr__(self):
        return f'Books {self.title}'

    def response(book):
        return jsonify({ 'id': book.id, 'title': book.title, 'author': book.author })