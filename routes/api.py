from flask import Blueprint, jsonify,make_response
import json
from app import app
api = Blueprint('api',__name__)
from app.Models import User
from app.Views import UserAPI, RegisterAPI, LoginAPI, PostAPI
from helpers import register_api


register_api(UserAPI, 'user_api', '/users', pk='id', version='v1')
register_api(RegisterAPI, 'register_api', '/auth/register', pk='id', version='v1')
register_api(LoginAPI, 'login_api', '/auth/login', pk='id', version='v1')
register_api(PostAPI, 'post_api', '/posts', pk='id', version='v1')

# app.add_url_rule('/users', view_func=UserAPI.as_view('users'))
# @api.route('/users')
# def index():
# 	user = user = User.query.filter_by(id=1).first()
# 	token =user.encodeAuthToken(user.id)
# 	return jsonify({
# 		'access_token': token.decode("utf-8")
# 	})

# @jwt.error_handler
# def error_handler(e):
#     return "Something bad happened", 400