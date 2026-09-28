from django.shortcuts import render, redirect
from .models import Product, Order


def home(request):
    products = Product.objects.all()
    cart = request.session.get('cart', {})

    cart_count = sum(cart.values())

    return render(request, 'productsapp/home.html', {
        'products': products,
        'cart_count': cart_count
    })
def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)

    return render(request, 'productsapp/product_detail.html', {
        'product': product
    })


def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)

    cart = request.session.get('cart', {})
    product_id = str(product_id)

    current_quantity = cart.get(product_id, 0)

    if current_quantity < product.stock:
        cart[product_id] = current_quantity + 1

    request.session['cart'] = cart

    return redirect('home')


def update_cart(request, product_id, action):
    cart = request.session.get('cart', {})
    product_id = str(product_id)

    if product_id in cart:
        product = Product.objects.get(id=product_id)

        if action == 'increase':
            if cart[product_id] < product.stock:
                cart[product_id] += 1

        elif action == 'decrease':
            cart[product_id] -= 1

            if cart[product_id] <= 0:
                del cart[product_id]

    request.session['cart'] = cart

    return redirect('cart')


def cart(request):
    cart = request.session.get('cart', {})
    products = Product.objects.filter(id__in=cart.keys())

    cart_items = []
    grand_total = 0

    for product in products:
        quantity = cart.get(str(product.id), 0)

        cart_items.append({
            'product': product,
            'quantity': quantity,
            'total': product.price * quantity
        })
        grand_total += product.price * quantity

    return render(request, 'productsapp/cart.html', {
    'cart_items': cart_items,
    'grand_total': grand_total
})


def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})
    product_id = str(product_id)

    if product_id in cart:
        del cart[product_id]

    request.session['cart'] = cart

    return redirect('cart')
def checkout(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')

        cart = request.session.get('cart', {})
        products = Product.objects.filter(id__in=cart.keys())

        grand_total = 0

        for product in products:
            quantity = cart.get(str(product.id), 0)
            grand_total += product.price * quantity

        Order.objects.create(
            name=name,
            email=email,
            phone=phone,
            address=address,
            total_amount=grand_total
        )

        request.session['cart'] = {}

        return render(request, 'productsapp/order_success.html', {
            'name': name,
            'total': grand_total
        })

    return render(request, 'productsapp/checkout.html')
from django.contrib.auth.models import User
from django.contrib.auth import login


def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.create_user(
            username=username,
            password=password
        )

        login(request, user)

        return redirect('home')

    return render(request, 'productsapp/signup.html')
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        from django.contrib.auth import authenticate, login

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')

        return render(request, 'productsapp/login.html', {
            'error': 'Invalid username or password'
        })

    return render(request, 'productsapp/login.html')


def logout_view(request):
    from django.contrib.auth import logout

    logout(request)

    return redirect('home')
def order_tracking(request):
    email = request.GET.get('email')

    orders = []

    if email:
        orders = Order.objects.filter(email=email).order_by('-created_at')

    return render(request, 'productsapp/order_tracking.html', {
        'orders': orders,
        'email': email
    })