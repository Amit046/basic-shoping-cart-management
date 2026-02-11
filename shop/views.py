from django.shortcuts import render, redirect

PRODUCTS = [
    {
        'id': 1,
        'name': 'Laptop',
        'price': 45000,
        'image': 'images/product1.jpg'
    },
    {
        'id': 2,
        'name': 'Smartphone',
        'price': 25000,
        'image': 'images/product2.jpg'
    },
    {
        'id': 3,
        'name': 'Wireless Headphones',
        'price': 3000,
        'image': 'images/product3.jpg'
    },
]


def home(request):
    cart = request.session.get('cart', {})
    
    cart_items = []
    total_price = 0
    
    for product_id, quantity in cart.items():
        product = next((p for p in PRODUCTS if str(p['id']) == product_id), None)
        if product:
            cart_items.append({
                'id': product['id'],
                'name': product['name'],
                'price': product['price'],
                'quantity': quantity,
                'subtotal': product['price'] * quantity
            })
            total_price += product['price'] * quantity
    
    context = {
        'products': PRODUCTS,
        'cart_items': cart_items,
        'total_price': total_price,
        'cart_count': len(cart_items)
    }
    
    return render(request, 'home.html', context)


def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})
    
    product_id_str = str(product_id)
    
    if product_id_str in cart:
        cart[product_id_str] += 1
    else:
        cart[product_id_str] = 1
    
    request.session['cart'] = cart
    
    return redirect('home')


def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})
    
    product_id_str = str(product_id)
    
    if product_id_str in cart:
        del cart[product_id_str]
    
    request.session['cart'] = cart
    
    return redirect('home')
