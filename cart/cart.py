# class Cart():
# 	def __init__(self, request):
# 		self.session = request.session

# 		# Get the current session key if it exists
# 		cart = self.session.get('session_key')

# 		# If the user is new, no session key!  Create one!
# 		if 'session_key' not in request.session:
# 			cart = self.session['session_key'] = {}


# 		# Make sure cart is available on all pages of site
# 		self.cart = cart

# 	def add(self, product):
# 		product_id = str(product.id)

# 		# Logic
# 		if product_id in self.cart:
# 			pass
# 		else:
# 			self.cart[product_id] = {'price': str(product.price)}

# 		self.session.modified = True

# 	def __len__(self):
# 		return len(self.cart)
from nutritiStore.models import Product

class Cart():
    def __init__(self, request):
        self.session = request.session
        self.cart_product_id = self.session.get('cart_product_id')

    def add(self, product):
        self.cart_product_id = product.id
        self.session['cart_product_id'] = self.cart_product_id
        self.session.modified = True

    def get_product(self):
        if self.cart_product_id:
            return Product.objects.get(id=self.cart_product_id)
        return None

    def __len__(self):
        return 1 if self.cart_product_id else 0


