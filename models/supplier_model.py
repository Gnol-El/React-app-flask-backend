class Supplier:

	def __init__(self, supplier_id=0, supplier_name='', contact_name='', address='', city='', postal_code=0, country='', phone=''):
		self.supplier_id = supplier_id
        self.supplier_name = supplier_name
        self.contact_name = contact_name
        self.address = address
        self.city = city
        self.postal_code = postal_code
        self.country = country
        self.phone = phone
    def serialize(self):
    	return{
    		'supplier_id' = self.supplier_id,
	        'supplier_name' = self.supplier_name,
	        'contact_name' = self.contact_name,
	        'address' = self.address,
	        'city' = self.city,
	        'postal_code' = self.postal_code,
	        'country' = self.country,
	        'phone' = self.phone
    	}