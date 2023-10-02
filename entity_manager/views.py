from django.shortcuts import render, HttpResponse
from .models import *

# Create your views here.
def index(request):
    # type = request.GET.get('type')
    # xdata = UniversalEntities.objects.filter(xtype__name = type)
    return render(request, 'index.html')
