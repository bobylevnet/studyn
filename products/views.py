from django.shortcuts import render

# Create your views here.
def index(request):
    context = {'title': 'Store'}
    return render(request, 'products/index.html')

def products(request):
    context = {
        'title': 'Store - Каталог',
        'products': [
            {'name': 'Test1', 'price': 1500, 'description': ' 8888888 8 8 8 8 8 '},
            {'name': 'Test2', 'price': 2900, 'description': ' 8888888 8 8 8 8 8 '},
            {'name': 'Test3', 'price': 3568, 'description': ' 8888888 8 8 8 8 8 '},
        ]

    }
    return render(request, 'products/products.html', context)
