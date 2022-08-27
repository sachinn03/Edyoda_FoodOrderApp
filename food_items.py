# This class is used for defining the attributes of Food Items

class Food_Items:
    def __init__(self,food_id,food_name,food_price,food_qty,food_discount,food_stock):
        self.food_id = food_id
        self.food_name = food_name
        self.food_price = food_price
        self.food_qty = food_qty
        self.food_discount = food_discount
        self.food_stock = food_stock
    
    def __str__(self):
        return "f Food Id :{self.food_id}\nFood Name :{self.food_name}\nFood Price :{self.food_price}\nFood Quantity :{self.food_qty}\nFood Discount :{self.food_discount}\nFood Stock :{self.food_stock}\n"

    def get_food_id(self):
        return self.food_id

    def set_food_id(self,food_id):
        self.food_id = food_id
    
    def get_food_name(self):
        return self.food_name
        
    def set_food_id(self,food_name):
        self.food_name = food_name

    def get_food_price(self):
        return self.food_price
        
    def set_food_price(self,food_price):
        self.food_price = food_price
    
    def get_food_qty(self):
        return self.food_qty
        
    def set_food_qty(self,food_qty):
        self.food_qty = food_qty

    def get_food_discount(self):
        return self.food_discount
        
    def set_food_discount(self,food_discount):
        self.food_discount = food_discount

    def get_food_stock(self):
        return self.food_stock
        
    def set_food_discount(self,food_stock):
        self.food_stock = food_stock