from django.shortcuts import render, redirect

def novedades(request):
    template = 'novedades.html'
    return render(request, template)