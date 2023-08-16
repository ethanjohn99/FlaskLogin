from application import app
from flask import Flask
from flask_bcrypt import Bcrypt

application = Flask(__name__)

bcrypt = Bcrypt(application)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
 
