from django.shortcuts import render, redirect, get_object_or_404
from .cart import Cart
from .forms import CheckoutForm
from nutritiStore.models import Product
from django.http import JsonResponse

def cart_summary(request):
    cart = Cart(request)
    cart_items = [] 
    
    for product_id, quantity in cart.cart.items():
        product = Product.objects.get(id=product_id)
        cart_items.append({
            'product': product,
         
        })

    total_amount = cart.calculate_total() 

    return render(request, "cart_summary.html", {'cart_items': cart_items, 'total_amount': total_amount})




def cart_add(request):
	cart = Cart(request)

	if request.POST.get('action') == 'post':

		product_id = int(request.POST.get('product_id'))
		

		product = get_object_or_404(Product, id=product_id)
		

		cart.add(product=product)


		response = JsonResponse({'Product Name: ': product.name})
		return response

def checkout_view(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            # Procesar la información del formulario de checkout
            # Ejemplo: Guardar la información del pedido en la base de datos
            # Generar número de pedido (aquí deberías implementar tu lógica específica)
            # Redirigir a la página de éxito del pedido
            return redirect('order_success')
    else:
        form = CheckoutForm()
    
    # Obtener el producto seleccionado para mostrar en el checkout
    product_id = 1  # ID del producto seleccionado (debe ajustarse según tus productos)
    product = Product.objects.get(id=product_id)  # Obtener el producto desde la base de datos
    
    return render(request, 'checkout.html', {'form': form, 'product': product})

def order_success_view(request):
    # Lógica para mostrar la página de éxito del pedido
    return render(request, 'order_success.html', {})


