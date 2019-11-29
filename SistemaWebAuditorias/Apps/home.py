from django.shortcuts import render


def home(request):
    template = 'index.html'
    return render(request, template)

def auditoria(request):
    template = 'Auditorias/home.html'
    return render(request, template)