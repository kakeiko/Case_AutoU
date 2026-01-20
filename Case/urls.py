from django.urls import path
import Case.views as views


urlpatterns = [
    path('', views.index, name='index'),
    path('resultado/<int:id>/', views.resultado, name='resultado'),
]