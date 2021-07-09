class Category:

	def __init__(self, category_id=0, category_name='', description=''):
		self.category_id = category_id
		self.category_name = category_name
		self.description = description

	def serialize(self):
		return{
			'category_id' = self.category_id,
			'category_name' = self.category_name,
			'description' = self.description
		}