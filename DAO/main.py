from bootstrap import db
from DAO.books import Books

class Main:

    def __init__(self):
        db.create_all()