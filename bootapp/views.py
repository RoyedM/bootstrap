from django.shortcuts import render

# Create your views here.

def home(request):
    """Display the index page"""
    return render(request, "index.html")