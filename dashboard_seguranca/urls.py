from django.urls import path
from .views import dashboard_geral

urlpatterns = [
    path('geral/', dashboard_geral, name='dashboard_principal'),
]