from django.shortcuts import render
from .models import Flight_Routes
# Create your views here.

def index(request):
    return render(request, 'searchRoutes/index.html')

def Flight_Routes_Fun(request):
    routes_list = Flight_Routes.objects.order_by('airline_ID')
    routes_dict = {'Routes': routes_list}
    return(render(request, 'searchRoutes/avaRoutes.html', context=routes_dict))
