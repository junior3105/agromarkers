from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

def index(request):
    return render(request, 'app/index.html')  # Renderiza o template 'app/index.html'
