from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configuring SQLite database (you can use PostgreSQL, MySQL, etc. instead)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://default:6zG1WeAguJoP@ep-little-bush-a46q76gm.us-east-1.aws.neon.tech:5432/verceldb?sslmode=require"

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# Initializing the database
db = SQLAlchemy(app)

from application.routes.routes import routes
app.register_blueprint(routes)
