from . import views
from django.urls import path

urlpatterns = [    
    path('',views.home_view),
    path('material_list', views.material_List),
    path('create_material', views.create_Material),
    path('material_update/<uuid:id>', views.material_Update),
    #path('material_delete/<uuid:id>', views. material_Delete),
    path('master_page',views.master_Page)
]