from django.shortcuts import render, redirect
from .models import Order, Product

def index(request):
    context = {
        "all_products": Product.objects.all()
    }
    return render(request, "store/index.html", context)

def buy(request):
    if request.method == "POST":
        product_id = request.POST.get("product_id")
        quantity_from_form = int(request.POST.get("quantity", 1))
        
        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return redirect("/")
            
        total_charge = quantity_from_form * float(product.price)
        
        Order.objects.create(quantity_ordered=quantity_from_form, total_price=total_charge)
        
        request.session['last_charge'] = total_charge
        
        return redirect("/checkout")
        
    return redirect("/")

def checkout(request):
    if 'last_charge' not in request.session:
        return redirect("/")
        
    all_orders = Order.objects.all()
    total_quantity_combined = 0
    total_amount_combined = 0.0
    
    for order in all_orders:
        total_quantity_combined += order.quantity_ordered
        total_amount_combined += float(order.total_price)
        
    context = {
        "last_charge": request.session['last_charge'],
        "total_items": total_quantity_combined,
        "total_spent": total_amount_combined
    }
    return render(request, "store/checkout.html", context)