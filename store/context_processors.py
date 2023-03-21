from .cart import Cart

def cart(request):  # to make cart globally available context_processord.py used
    return {'cart': Cart(request)}
    