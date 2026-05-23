from django.shortcuts import render
from .models import Category, Product

def Home(request):
    return render(request, " Home.html")


def home(request):
    categories = Category.objects.all()
    return render(request, "Home.html", {"categories": categories})


from django.shortcuts import render
from .models import Product

def home(request):
    products = Product.objects.all()
    return render(request, "home.html", {"products": products})



from django.shortcuts import render
from .models import Product
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Cart, CartItem


def shop(request):
    products = Product.objects.all()
    return render(request, "shop.html", {"products": products})



def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    cart, created = Cart.objects.get_or_create(user=request.user)

    item, created = CartItem.objects.get_or_create(
        cart=cart,
        product=product,
        defaults={"quantity": 1}
    )

    if not created:
        item.quantity += 1
        item.save()

    return redirect("cart")



def cart(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    items = cart.items.all()

    total = sum(item.total_price() for item in items)

    return render(request, "cart.html", {
        "items": items,
        "total": total
    })



def increase_qty(request, item_id):
    item = get_object_or_404(CartItem, id=item_id)
    item.quantity += 1
    item.save()
    return redirect("cart")


def decrease_qty(request, item_id):
    item = get_object_or_404(CartItem, id=item_id)

    if item.quantity > 1:
        item.quantity -= 1
        item.save()
    else:
        item.delete()

    return redirect("cart")


def remove_from_cart(request, item_id):
    item = get_object_or_404(CartItem, id=item_id)
    item.delete()
    return redirect("cart")


def checkout(request):
   
    return render(request, "checkout.html", )

def contact(request):
   
    return render(request, "contact.html", )
