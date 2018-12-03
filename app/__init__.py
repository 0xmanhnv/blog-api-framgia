import click
from flask import Flask , jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate, MigrateCommand
from flask_jwt import JWT, jwt_required, current_identity
from flask_cors import CORS, cross_origin

app = Flask(__name__)
#load config 
app.config.from_object('config')
bcrypt = Bcrypt(app)

#connect database
db = SQLAlchemy(app)
ma = Marshmallow(app)


#import models to app
from app.Models import *
import routes.api
#connect database with migrate
migrate = Migrate(app, db)

# from helpers.jwt import authenticate, identity
# JWT(app, authenticate, identity)

cors = CORS(app, resources={r"/api/*": {"origins": "*", "Access-Control-Allow-Origin": "*" }})

@app.errorhandler(404)
def page_not_found(e):
	res = {
		"error": {
			"message": "Unknown path components: " + str(request.full_path)
		},
		"method": request.method
	}
	return jsonify(res), 404
