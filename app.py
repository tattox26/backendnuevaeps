from flask import Flask
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from config import Config
from db import close_db
from auth.routes import auth, bcrypt

app = Flask(__name__)
app.config.from_object(Config)

CORS(app)
JWTManager(app)
bcrypt.init_app(app)  # Aquí se inicializa bcrypt correctamente
#from auth.routes import auth
from solicitudes.routes import solicitudes

app.register_blueprint(auth)
app.register_blueprint(solicitudes)

app.teardown_appcontext(close_db)

if __name__ == '__main__':
    app.run(debug=True)
