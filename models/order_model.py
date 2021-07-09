class Order:

    def __init__(self, order_id=0, customer_id_id=0, employee_id_id=0, order_date='', shipper_id=0):
        self.order_id = order_id
        self.customer_id = customer_id
        self.employee_id = employee_id
        self.order_date = order_date
        self.shipper_id = shipper_id

    def serialize(self):
        return {
            'order_id': self.order_id,
            'customer_id': self.customer_id,
            'employee_id': self.employee_id,
            'order_date': self.order_date,
            'shipper_id': self.shipper_id
        }