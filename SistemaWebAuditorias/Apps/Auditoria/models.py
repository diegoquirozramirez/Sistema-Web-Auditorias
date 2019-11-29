from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class auditoria(models.Model):
    codigo = models.CharField(max_length=20)
    nombre = models.CharField(max_length=20)
    ubic = models.CharField(max_length=20)
    level_risk = models.IntegerField()
    init_date = models.DateField()
    fini_date = models.DateField()
    inform = models.FileField(upload_to='media/informes/')

    def convo(self):
        estado = convocatoria.objects.filter(auditoria_id=self.id).values('estado')
        return '{}'.format(estado[0]['estado'])

class convocatoria(models.Model):
    auditoria = models.ForeignKey(auditoria, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    estado = models.BooleanField(default=False)

    class Meta:
        unique_together = ('auditoria','user')

    def __str__(self):                   
        return '{} {} {}'.format(self.auditoria.nombre, self.user, self.estado)

    def state(self):
        if self.estado == False:
            state = 'En espera'
        if self.estado == True:
            state = 'Aceptado' 
        return '{}'.format(state)
    
