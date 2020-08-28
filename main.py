from bootstrap import app, db
import routes
from DAO.main import Main as MainDAO

teste = MainDAO()
app.run()