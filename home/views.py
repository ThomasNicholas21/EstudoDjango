from django.shortcuts import render

# Create your views here.
def home_view(request):
    context = {
        'variavel': 'Isso é uma variável utilizando a função render',
        'title': 'Home'
    }
    return render(request, 'home/index.html', context)
