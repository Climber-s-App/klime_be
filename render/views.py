from django.shortcuts import render

def index(request):
    return render(request, 'render/index.html')

# Create your views here.
