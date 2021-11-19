from django.shortcuts import render
from cars.models import Transport, CategoryTransport

# Create your views here.

def transportView(request):
    transports = Transport.objects.all()
    categories = CategoryTransport.objects.all()
    
    return render(request, 'cars/home.html', {'transports': transports, 'categories': categories})


def transportDetailView(request, slug):
    transport = Transport.objects.get(slug=slug)
    return render(request, 'cars/cars_detail.html', {'transport': transport})


def categoryDetailView(request, pk):
    transports = Transport.objects.filter(category_id=pk)
    return render(request, 'cars/category_detail.html', {'transports': transports})