from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configuring SQLite database (you can use PostgreSQL, MySQL, etc. instead)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# Initializing the database
db = SQLAlchemy(app)

from application.routes.routes import routes
app.register_blueprint(routes)
