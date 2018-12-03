from flask.views import MethodView
from flask import request, make_response, jsonify, g
from app.Models import Category, category_schema, categories_schema
from helpers import token_required, slugify, custom_response
from app import db

class CategoryAPI(MethodView):
	"""
	"" get info categories 
	"" return: object or array
	"""
	def get(self, id=None):
		#get param page request
		try:
			page = int(request.args.get('page', 1))
			limit = int(request.args.get('limit', 10))
		except:
			page = 1
			limit =10
		if not id:
			try:
				#query get data from database 
				categories_paginate = Category.query.paginate(page, limit)
				categories = categories_paginate.items

				res = {}
				data = []

				res.update({
					"data": categories_schema.dump(categories).data
				})

				#paging 
				url_previous = ""
				url_next =  ""
				paging = {}

				if categories_paginate.has_next:
					url_next = APP_URL +"/api/v1/categories?page=" + str((page + 1)) + "&limit="+str(limit)
					paging.update({"next": url_next})
				if categories_paginate.has_prev:
					url_previous = APP_URL +"/api/v1/categories?page=" + str((page - 1)) + "&limit="+str(limit)
					paging.update({"previous": url_previous})

				#response
				res.update({
					"paging": paging,
					"pages": categories_paginate.pages,
					"per_page": page,
					"next_num": categories_paginate.next_num,
					"prev_num": categories_paginate.prev_num,
					"limit": limit
				})
			except Exception as e:
				# "error": e.get_description(),
				res = {
					"data": []
				}
				return jsonify(res)
		else:
			category = Category.query.filter_by(id=id).first()
			if not category:
				res = {
					"error": {
						"message": "Unsupported get request. Object with ID " + str(id)+" does not exist"
					}
				}
				return jsonify(res), 404
			res = category_schema.dump(category).data
		return make_response(jsonify(res))

	#create category
	@token_required
	def post(self):
		#get data from client
		try:
			data = request.get_json()
			category = Category(
				name = data.get('name'),
				thumbnail = data.get('thumbnail'),
				slug = slugify(data.get('name')),
				description = data.get('description'),
				user_id = g.user.id,
				status = data.get('status', 1),
				parent_id = data.get('parent_id')
			)
			db.session.add(category)
			db.session.commit()

			res = {
				"status": "ok",
				"code": 200,
				"message": "The post was successfully added",
				"category": category_schema.dump(category).data
			}
			return make_response(jsonify(res)), 200
		except Exception as e:
			res = {
				"status": "fail",
				"code": 400,
				"message": "failed",
			}
			return make_response(jsonify(res)), 400