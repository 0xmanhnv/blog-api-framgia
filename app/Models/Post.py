from app import db, ma
from sqlalchemy.dialects.mysql import INTEGER,TINYINT
from sqlalchemy import *
import datetime

class Post(db.Model):
	__tablename__ = 'posts'
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(255), nullable=False)
	slug = db.Column(db.String(255),unique=True, nullable=False)
	thumbnail = db.Column(db.String(255), nullable=True)
	description = db.Column(db.Text(), nullable=True)
	content = db.Column(db.Text(), nullable=False)
	status = db.Column(TINYINT(), doc="0. private, 1.public",server_default="1", nullable=False)
	view_count = db.Column(db.Integer)
	category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
	user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
	created_at = db.Column(db.TIMESTAMP(), nullable=True, server_default=db.func.now())
	updated_at = db.Column(db.TIMESTAMP(), nullable=True, server_onupdate=db.func.now())

	# funtion 
	def delete(self):
		db.session.delete(self)
		db.session.commit()
	def update(self, data):
		for key, item in data.items():
			setattr(self, key, item)
		self.updated_at = datetime.datetime.utcnow()
		db.session.commit()
	@staticmethod
	def get_one_user(id):
		return Post.query.get(id)

	"""
	"Chuyển các thuộc tính về thành chuỗi
	"""
	def __repr__(self):
		return str(self.__dict__)
"""
"Tạo Schema cho model
"""
class PostSchema(ma.ModelSchema):
	class Meta:
		fields = ('id','title', 'thumbnail', 'slug', 'description', 'content', 'status', 'user_id', 'category_id', 'view_count')

posts_schema = PostSchema(many=True)
post_schema = PostSchema()