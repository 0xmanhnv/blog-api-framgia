from flask.views import MethodView
from app.Models import User
from helpers import token_required
from flask import g

class UserAPI(MethodView):
	@token_required
	def get(self, id=None):
		return "User.query.all()"