from app import db, app, ma
from sqlalchemy.dialects.mysql import INTEGER,TINYINT

class Category(db.Model):
	__tablename__ = 'categories'
	id = db.Column(db.Integer, primary_key=True)
	parent_id = db.Column(db.Integer, nullable=True)
	name = db.Column(db.String(255), nullable=False)
	user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
	slug = db.Column(db.String(255),unique=True, nullable=False)
	thumbnail = db.Column(db.String(255), nullable=True)
	description = db.Column(db.Text(), nullable=True)
	# status = db.Column(TINYINT(), doc="0. private, 1.public",server_default="1", nullable=False)
	status = db.Column(db.Numeric(4, asdecimal=False), doc="0. private, 1.public",server_default="1", nullable=False)
	created_at = db.Column(db.TIMESTAMP(), nullable=True, server_default=db.func.now())
	updated_at = db.Column(db.TIMESTAMP(), nullable=True, server_default=db.func.now(), server_onupdate=db.func.now())
	deleted_at = db.Column(db.TIMESTAMP(), nullable=True)

	"""
	"Chuyển các thuộc tính về thành chuỗi
	"""
	def __repr__(self):
		return str(self.__dict__)

#Tạo Schema cho model
class CategorySchema(ma.ModelSchema):
	class Meta:
		fields = ('id','parent_id','name', 'user_id','slug', 'thumbnail', 'description','status', 'created_at','updated_at')

category_schema = CategorySchema()
categories_schema = CategorySchema(many=True)