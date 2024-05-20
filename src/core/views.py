from django.shortcuts import render

# Create your views here.
def index(request):
    context = {}

    context['type_investor'] = 'Moderado'

    return render(request, "home.html", context)