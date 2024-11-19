from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="gastos"),
    path('add-gastos', views.add_gastos, name="add-gastos")
]