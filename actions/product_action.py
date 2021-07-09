import sqlite3

from ..models import product_model

class ProductAction:

    def __init__(self, db_connection) -> None:
        self.db_connection = db_connection

    def get_all(self):
        conn = sqlite3.connect(self.db_connection)
        cursor = conn.cursor()
        sql = 'SELECT * FROM tbl_product'
        cursor.execute(sql)
        rows = cursor.fetchall()
        result = []
        for row in rows:
            product = product_model.Product(
                product_id=row[0],
                product_name=row[1],
                supplier_id=row[2],
                category_id=row[3],
                amount=row[4],
                price=row[5]
            )
            result.append(product.serialize())
        return result, 200

    def get_by_id(self, id):
        conn = sqlite3.connect(self.db_connection)
        cursor = conn.cursor()
        sql = """
            SELECT * FROM tbl_product WHERE product_id = ?
        """
        cursor.execute(sql, (id, ))
        row = cursor.fetchone()
        if row == None:
            return 'Product not found', 404
        product = product_model.Product(
            product_id=row[0],
            product_name=row[1],
            supplier_id=row[2],
            category_id=row[3],
            amount=row[4],
            price=row[5]
        )
        return product, 200

    def add(self, product: product_model.Product):
        conn = sqlite3.connect(self.db_connection)
        cursor = conn.cursor()
        sql = """
            INSERT INTO tbl_product
            VALUES(null, ?, ?, ?, ?, ?)
        """
        cursor.execute(sql, (product.product_name, product.supplier_id, product.category_id, product.amount, product.price))
        conn.commit()
        return 'Inserted successfully!'

    def update(self, id: int, product: product_model.Product):
        conn = sqlite3.connect(self.db_connection)
        cursor = conn.cursor()
        sql = """
            UPDATE tbl_product
            SET product_name = ?, supplier_id = ?, category_id = ?, amount = ?, price = ?
            WHERE product_id = ?
        """
        cursor.execute(sql, (product.product_name, product.supplier_id, product.category_id, product.amount, product.price, id))
        conn.commit()
        n = cursor.rowcount
        if n == 0:
            return 'Product not found', 404
        return 'Updated successfully', 200