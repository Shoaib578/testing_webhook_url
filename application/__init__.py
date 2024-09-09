from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configuring SQLite database (you can use PostgreSQL, MySQL, etc. instead)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://default:vHJECA8KoqQ3@ep-shrill-rain-a43ssyi5.us-east-1.aws.neon.tech:5432/verceldb?sslmode=require"


# Initializing the database
db = SQLAlchemy(app)

from application.routes.routes import routes
app.register_blueprint(routes)
