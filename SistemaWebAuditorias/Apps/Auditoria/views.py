from django.shortcuts import render, redirect
from django.urls import reverse
from django.db import IntegrityError
from Apps.Auditoria.models import auditoria, convocatoria


# Create your views here.
def listAuditorias(request):
    #queryset
    audit = auditoria.objects.all()
    contexto = {'audit':audit}
    template = 'Auditorias/listAuditorias.html'
    return render(request, template, contexto)

def listConvo(request):
    #queryset
    audit = auditoria.objects.all()    
    convo = convocatoria.objects.all()
    contexto = {'audit':audit, 'convo':convo}
    template = 'Auditorias/convocatorias.html'
    return render(request, template, contexto)

def convo(request, idaudit):
    try:
        c = convocatoria(
            auditoria_id=idaudit,
            user_id=request.user.id,        
        ) 
        c.save()
        return redirect('Auditorias:listconvo')
    except IntegrityError as e:
        return redirect('Auditorias:listconvo')
    #return redirect(reverse('Auditorias:listconvo', args=str(idaudit)))

