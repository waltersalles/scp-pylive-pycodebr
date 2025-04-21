from django.shortcuts import render
from products.models import Product

def product_view(request):
    products = Product.objects.all ()

    return render(
        request=request,
        template_name='products.html',
        context={'products': products},
    )
        
        
