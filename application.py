from application import app,db


from application.routes.routes import routes
app.register_blueprint(routes)


# Create the database and tables
with app.app_context():
    db.create_all()


if __name__ == '__main__':
    app.run(debug=True,port=80)