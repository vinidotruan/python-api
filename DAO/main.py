from bootstrap import db
from DAO.book import Book
from DAO.client import Client
from DAO.reserve import Reserve

class Main:

    def __init__(self):
        db.create_all()