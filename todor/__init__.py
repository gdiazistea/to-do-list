from flask import Flask, render_template

def create_app():
    app = Flask(__name__)

    # Load configuration from a file

    app.config.from_mapping(
        DEBUG = True,
        SECRETE_KEY = 'dev')
    
    # Register blueprints

    from . import todo
    app.register_blueprint(todo.bp)

    from . import auth
    app.register_blueprint(auth.bp)

    @app.route('/')
    def index():
        return render_template('index.html')
    
    return app