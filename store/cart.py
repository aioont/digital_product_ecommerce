from django.conf import settings

from .models import Product

class Cart(object):
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)

        if not cart:          #check if cart aleady exist
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def __iter__(self):
        for p in self.cart.keys(): # iterate through keys in the session that is product
            self.cart[str(p)]['product'] = Product.objects.get(pk=p) # all info about product insert into self.cart[str(p)]['product'] 

        for item in self.cart.values():
            item['total_price'] = int(item['product'].discount_price * item['quantity']) 

            yield item #The yield statement suspends a function’s execution and sends a value back to the caller, but retains enough state to enable the function to resume where it left o
    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modeified = True

    def add(self, product_id, quantity=1, update_quantity=False):
        product_id = str(product_id)

        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': int(quantity), 'id': product_id}
        
        if update_quantity:
            self.cart[product_id]['quantity'] += int(quantity) # take product from session and quantity from variable

            if self.cart[product_id]['quantity'] == 0:
                self.remove(product_id)
            
        self.save()
    
    def remove(self, product_id):
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()
    
    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True
    
    def get_total_cost(self):
        for p in self.cart.keys():
            self.cart[str(p)]['product'] = Product.objects.get(pk=p)

        return int(sum(item['product'].discount_price * item['quantity'] for item in self.cart.values()))  # price * quantity for each item
    
    def get_item(self, product_id):
        if str(product_id) in self.cart:
            return self.cart[str(product_id)]
        else:
            return None

 
