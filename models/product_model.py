class Product:

	def __init__(self, product_id=0, product_name='', supplier_id=0, category_id=0, amount='', price=0):
		self.product_id = product_id
		self.product_name = product_name
		self.supplier_id = supplier_id
		self.category_id = category_id
		self.amount = amount
		self.price = price

	def serialize(self):
		return{
			'product_id' : self.product_id,
			'product_name' : self.product_name,
			'supplier_id' : self.supplier_id,
			'category_id' : self.category_id,
			'amount' : self.amount,
			'price' : self.price
    	}