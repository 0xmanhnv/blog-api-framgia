from flask.views import MethodView
from app.Models import User
from helpers import token_required
from flask import g, Blueprint, request, make_response, jsonify

class AuthUserAPI(MethodView):
	@token_required
	def get(self, id=None):
		# get the auth token
		auth_header = request.headers.get('Authorization')
		if auth_header:
			# auth_token = auth_header.split(" ")[1]
			auth_token = auth_header
		else:
			auth_token = ''
		if auth_token:
			resp = User.decodeAuthToken(auth_token)
			if not isinstance(resp, str):
				user = User.query.filter_by(id=resp).first()
				responseObject = {
					'status': 'success',
					'user': {
						'user_id': user.id,
						'email': user.email
					}
				}
				return make_response(jsonify(responseObject)), 200
			responseObject = {
				'status': 'fail',
				'message': resp
			}
			return make_response(jsonify(responseObject)), 401
		else:
			responseObject = {
				'status': 'fail',
				'message': 'Provide a valid auth token.'
			}
			return make_response(jsonify(responseObject)), 401
