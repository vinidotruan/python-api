from bootstrap import app, db, jsonify
from datetime import date

class Reserve(db.Model):
    __tablename__ = "reserves"

    id = db.Column(db.Integer, primary_key=True)
    date_out = db.Column(db.Date, unique=False, nullable=False)
    date_back = db.Column(db.Date, unique=False, nullable=True)
    client_id = db.Column(db.Integer, db.ForeignKey('clients.id'), nullable=False)
    client = db.relationship('Client', backref=db.backref('reserves'))
    book_id = db.Column(db.Integer, db.ForeignKey('books.id'), nullable=False)
    book = db.relationship('Book', backref=db.backref('reserves'))

    def __repr__(self):
        return f'Reserve {self.id}'

    def response(reserve):
        return jsonify({
            'date_out': reserve.date_out,
            'date_back': reserve.date_back,
            'client_id': reserve.client_id,
            'book_id': reserve.book_id
        })

    def delayDay(reserve):
        calc =  date.today() - reserve.date_out
        return calc.days

    