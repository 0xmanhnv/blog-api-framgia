from functools import wraps
from app import app
from flask import request, jsonify, g, Response
import jwt
from app.Models import User
import json

"""
function register api
return: route
"""
def register_api(view, endpoint, url, pk='id', pk_type='int', version=None):
	if version:
		url_api = '/api/'+version+url
	else:
		url_api = '/api/v1/'+url
	view_func = view.as_view(endpoint)
	app.add_url_rule(url_api, defaults={pk: None},
		view_func=view_func, methods=['GET',])
	app.add_url_rule(url_api, view_func=view_func, methods=['POST',])
	app.add_url_rule('%s/<%s:%s>' % (url_api, pk_type, pk), view_func=view_func,
		methods=['GET', 'PUT', 'DELETE'])

"""
token required
"""
def token_required(f):
	@wraps(f)
	def decorated(*args, **kwargs):
		token = request.args.get('access_token', None)

		if 'Authorization' in request.headers:
			token = request.headers['Authorization']

		if not token:
			return jsonify({
				'message' : 'Token is missing!'
			}), 401

		try:
			data = jwt.decode(token, app.config.get('SECRET_KEY'))
			g.user = User.query.filter_by(id=data['user_id']).first()
		except:
			return jsonify({
				'message': 'Token is invalid!'
			}), 401
		return f(*args, **kwargs)
	return decorated

# create slug
import re
from unidecode import unidecode

_punct_re = re.compile(r'[\t !"#$%&\'()*\-/<=>?@\[\\\]^_`{|},.]+')


def slugify(text, delim=u'-'):
	"""Generates an ASCII-only slug."""
	result = []
	for word in _punct_re.split(text.lower()):
		result.extend(unidecode(word).split())
	return str(delim.join(result))

# custom_response
def custom_response(res, status_code):
	"""
	Custom Response Function
	"""
	return Response(
		mimetype="application/json",
		response=json.dumps(res),
		status=status_code
	)