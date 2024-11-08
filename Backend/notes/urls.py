from django.urls import path
from notes import views

app_name = 'notes'

urlpatterns = [
    path('', views.list_api),
    path('<int:pk>/', views.detail),
    path('create', views.create),
    path('delete', views.delete),
    path('update', views.update),
    path('contact', views.contact),
    path('count', views.count)
]