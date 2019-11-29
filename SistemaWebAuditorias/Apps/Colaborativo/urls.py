from django.urls import path
from Apps.Colaborativo import views

app_name = 'Colaborativo'

urlpatterns = [
   
   path('', views.goEspacioColaborativo, name="colaboracion"),
   path('update/<int:ida>', views.updateInfoAuditoria, name="update"),
]