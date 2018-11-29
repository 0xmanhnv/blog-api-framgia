from flask.views import MethodView
from app.Models import User
from flask import request, make_response,jsonify
from app import db

class RegisterAPI(MethodView):
	"""
	User Registration Resource
	"""
	def get(self, id=None):
		pass
	def post(self):
		# get the post data
		post_data = request.get_json()

		if post_data:
			# check if user already exists
			user = User.query.filter_by(email=post_data.get('email')).first()

			if not user:
				try:
					user= User(
						name = post_data.get('name'),
						email=post_data.get('email'),
						password=post_data.get('password'),
						username = post_data.get('username')
					)
					# insert to database
					db.session.add(user)
					db.session.commit()

					#genarate auth token
					auth_token = user.encodeAuthToken(user.id)

					responseObject	=	{
						'status': 'success',
						'message': 'Successfully registered',
						'access_token': auth_token.decode()
					}
					return make_response(jsonify(responseObject)), 200
				except Exception as e:
					print(e)
					responseObject = {
						'status': 'fail',
						'message': 'Some error occurred. Please try again.'
					}
						# 'access_token': auth_token.decode()
					return make_response(jsonify(responseObject)), 401
			else:
				responseObject = {
					'status' : 'fail',
					'message': 'User already exists. Please Log in.'
				}
				return make_response(jsonify(responseObject))
		else:
			responseObject = {
				'status': 'fail',
				'message': 'Some error occurred. Please try again.'
			}
				# 'access_token': auth_token.decode()
			return make_response(jsonify(responseObject)), 401