from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

# Initialize the database
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Load configuration from a file

    app.config.from_mapping(
        DEBUG = True,
        SECRETE_KEY = 'dev',
        SQLALCHEMY_DATABASE_URI = "sqlite:///todolist.db"
        )
    
    # Initialize the database with the app
    db.init_app(app)

    # Register blueprints
    from . import todo
    app.register_blueprint(todo.bp)

    from . import auth
    app.register_blueprint(auth.bp)

    @app.route('/')
    def index():
        return render_template('index.html')
    with app.app_context():
        # Create the database tables
        db.create_all()
    
    return app