from flask_jwt import JWT, jwt_required, current_identity
from app.Models import User

def authenticate(username, password):
	if not (username and password):
		return False
	user = User.query.filter_by(id=1).first()
	return user

def identity(payload):
    user_id = payload['identity']
    return {"user_id": user_id}