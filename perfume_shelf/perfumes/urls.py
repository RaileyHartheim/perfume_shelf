from django.urls import path

from . import views

app_name = 'perfumes'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.perfume_create, name='perfume_create'),
    path('perfume/<int:perfume_id>/edit',
         views.perfume_edit, name='perfume_edit'),
    path('perfume/<int:perfume_id>/delete/',
         views.perfume_delete, name='perfume_delete'),
    path('perfume/<int:perfume_id>/',
         views.perfume_detail, name='perfume_detail'),
]
