from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from cart.models import CartItem
from .models import Order

@login_required
def place_order(request):
    cart_items = CartItem.objects.filter(user=request.user)

    if not cart_items:
        return redirect('cart')

    total = sum(item.product.price * item.quantity for item in cart_items)

    order = Order.objects.create(
        user=request.user,
        total_amount=total
    )

    cart_items.delete()

    return redirect('payment', order_id=order.id)


@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'orders/order_history.html', {'orders': orders})


@login_required
def payment_page(request, order_id):
    order = Order.objects.get(id=order_id, user=request.user)
    return render(request, 'orders/payment.html', {'order': order})


@login_required
def payment_success(request, order_id):
    order = Order.objects.get(id=order_id, user=request.user)
    return render(request, 'orders/payment_success.html', {'order': order})
