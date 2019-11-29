from django.shortcuts import render, redirect
from Apps.Auditoria.models import auditoria
from Apps.Auditoria.forms import auditoriaForm

# Create your views here.
def goEspacioColaborativo(request):
    audit = auditoria.objects.all()
    context = {'audit':audit}
    template = 'Auditorias/Colaborativo/colaborativo.html'
    return render(request, template, context)

def updateInfoAuditoria(request, ida):
    audit = auditoria.objects.get(id=ida)
    
    if request.method == 'GET':
        form = auditoriaForm(instance=audit)
    else:
        form = auditoriaForm(request.POST, instance=audit)
        if form.is_valid():
            form.save()
        return redirect('Colaborativo:colaboracion')
    context = {'form':form}
    template = 'Auditorias/Colaborativo/update.html'
    return render(request, template, context)
