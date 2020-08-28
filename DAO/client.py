from bootstrap import app, db, jsonify
from DAO.reserve import Reserve

class Client(db.Model):
    __tablename__ = "clients"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=False, nullable=False)

    def __repr__(self):
        return f'Client {self.name}'

    def response(client):
        return jsonify({ 'id': client.id, 'name': client.name })