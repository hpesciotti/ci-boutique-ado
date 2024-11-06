from django.shortcuts import render
from django.contrib import messages
from .forms import OrderForm

# Create your views here.

def checkout(request):
    """
    """
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51QHr4UIJfcLvaiK6UM6DcSma03ZoiQNs0g5pL3PzsxnqeIp3x3mD3xLHogGtvU5jRYwCuG4am5IFDwix8XcyeRrS003pU2kkoz',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
