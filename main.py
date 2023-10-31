from db.model import app
from users.routes import router

# imports the endpoint urls from users/routes.py file
app.register_blueprint(router)

if __name__=='__main__':
    app.run(debug = True)           # for automatically bringing the change without restarting application debug is set to True