from . import views
from django.urls import path

urlpatterns = [    
    path('material_list', views.material_List, name='material_list'),
    path('create_material', views.create_Material, name='create_material'),
    path('material_update/<int:id>/', views.material_Update, name='material_update'),
    path('material_delete/<int:id>/', views. material_Delete, name='material_delete'),
]