from django.urls import path
from Apps.Auditoria import views

app_name = 'Auditorias'

urlpatterns = [
   path('listado', views.listAuditorias, name="auditorias"),
   path('listconvo', views.listConvo, name="listconvo"),
   path('convo/<int:idaudit>', views.convo, name="convo"),
]