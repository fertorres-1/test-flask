from flask import Flask
from flask_login import LoginManager
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)
Session = scoped_session(sessionmaker(bind=engine))

login_manager = LoginManager()
login_manager.login_view = 'auth.login'  # ruta del login

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'clave-super-secreta'

    from .models import Usuario
    from .routes import routes
    from .auth import auth

    app.register_blueprint(routes)
    app.register_blueprint(auth)

    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        with Session() as session:
            return session.query(Usuario).get(int(user_id))

    @app.teardown_appcontext
    def shutdown_session(exception=None):
        Session.remove()

    return app
