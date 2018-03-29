from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_pagedown import PageDown
from flask_moment import Moment
from flask_migrate import Migrate
from flask_login import LoginManager

bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
db = SQLAlchemy()
pagedown = PageDown()
migrate = Migrate()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'