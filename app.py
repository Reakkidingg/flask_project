import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

# Initialize the extensions
db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.login_message_category = 'info'

def create_app():
    app = Flask(__name__)

    # Configuration settings
    app.config['SECRET_KEY'] = '27b8ca823c7552cbb0a099e19cd7bb83'

    # Update this line with PostgreSQL connection details
    app.config['SQLALCHEMY_DATABASE_URI'] = (
        f"postgresql://flask_user:0412@localhost:5050/flask_blog_db"
    )

    # Initialize extensions
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    # Register blueprints
    from auth.routes import auth
    from blog.routes import blog
    app.register_blueprint(auth)
    app.register_blueprint(blog)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
