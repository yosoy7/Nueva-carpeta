from flask import Flask
from .routes import main_bp

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your-secret-key'
    
    # Register the blueprint
    app.register_blueprint(main_bp)
    
    return app