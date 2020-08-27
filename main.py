from bootstrap import app, db
from DAO.main import Main as MainDAO

teste = MainDAO()
app.run()