from flask.views import MethodView
from flask import request, make_response, jsonify
from app.Models import User

class LoginAPI(MethodView):
	"""
	User login resource
	"""
	def post(self):
		post_data = request.get_json()
		try:
			#fetch the user data
			user = User.query.filter_by(
				email=post_data.get('email')
			).first()

			if user and user.verifyPassword(post_data.get('password')):
				access_token = user.encodeAuthToken(user.id)
				if access_token:
					responseObject ={
						'status': 'success',
						'message': 'Successfully logged in.',
						'access_token': access_token.decode()
					}
					return make_response(jsonify(responseObject)), 200
			else:
				responseObject = {
					'status' : 'fail',
					'message' : 'User does not exist.'
				}
				return make_response(jsonify(responseObject)), 404
		except Exception as e:
			print(e)
			responseObject = {
				'status': 'fail',
				'message': 'try again'
			}
			return make_response(jsonify(responseObject)), 500