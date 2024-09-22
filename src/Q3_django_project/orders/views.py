from django.shortcuts import render
from .models import Order

def top_customers_view(request):
    # Call the top_customers method from the Order model
    top_customers = Order.top_customers()
    return render(request, 'orders/top_customers.html', {'top_customers': top_customers})
