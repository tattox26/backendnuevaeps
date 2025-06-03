from flask import Flask
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from config import Config
from db import close_db
from routes.auth import auth, bcrypt
from routes.medicamentos import medicamentos
from routes.solicitudes import solicitudes
app = Flask(__name__)
app.config.from_object(Config)

CORS(app)
JWTManager(app)
bcrypt.init_app(app)

app.register_blueprint(auth)
app.register_blueprint(solicitudes)
app.register_blueprint(medicamentos)

app.teardown_appcontext(close_db)

if __name__ == '__main__':
    app.run(debug=True)
