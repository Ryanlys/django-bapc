from django.shortcuts import render
from django.http import HttpRequest,Http404
from .models import Products
from django.views import generic

# Create your views here.
def home(request, *args, **kwargs):
    context = {
        "obj":Products.objects.all(),
    }
    return render(request, "home.html",context)