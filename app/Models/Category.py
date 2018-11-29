from app import db

class Category(db.Model):
	__tablename__ = 'categories'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(255), nullable=False)
	slug = db.Column(db.String(255),unique=True, nullable=False)
	thumbnail = db.Column(db.String(255), nullable=True)
	description = db.Column(db.Text(), nullable=True)
	created_at = db.Column(db.TIMESTAMP(), nullable=True, server_default=db.func.now())
	updated_at = db.Column(db.TIMESTAMP(), nullable=True, server_default=db.func.now(), server_onupdate=db.func.now())

	"""
	"Chuyển các thuộc tính về thành chuỗi
	"""
	def __repr__(self):
		return str(self.__dict__)