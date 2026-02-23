from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'message': 'Sua plataforma de gerenciamento de vulnerabilidades.',
    }
    return render(request, 'index.html', context)