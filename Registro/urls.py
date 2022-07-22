from django.urls import path, include
from . import views
from django.contrib.auth.views import login_required

urlpatterns = [
    
    # listar las carreras de la bd
    # localhost:8000/listarCarreras 
    path('listarCarreras', views.listar_carreras, name="listar_carreras"),

    # agregar una carrera
    # localhost:8000/agregar_carrera
    path('agregar_carrera', views.agregar_carrera, name="agregar_carrera"),    
    
    # # borrar una carrera
    # # localhost:8000/borrar_carrera/NUM
    # path('borrar_carrera/<int:carrera_id>', views.borrar_carrera, name="borrar_carrera"),

    # # editar una carrera
    # # localhost:8000/editar_carrera/NUM
    # path('editar_carrera/<int:carrera_id>', views.editar_carrera ,name="editar_carrera"),


  # editar una carrera
    path('editar_carrera/<int:carrera_id>', login_required(views.editar_carrera), name="editar_carrera"),

    # borrar una carrera
    path('borrar_carrera/<int:carrera_id>', login_required(views.borrar_carrera), name="borrar_carrera"),




    # OTROS LLAMADOS CON GENERICS
    # localhost:8000/add_carrera
    # path('add_carrera', views.CarreraCreate.as_view(), name="add_carrera"),

    # path('list_carreras', views.CarreraList.as_view(), name="list_carreras"),

    # Crear la ruta para eliminar y modificar por GENERICS    
       
     # llamando a la clases 
    path('add_carrera', views.CarreraCreate.as_view(), name="add_carrera"),

    path('list_carreras/', views.CarreraList.as_view(), name='list_carreras'),

    path('edit_carrera/<int:pk>', views.CarreraUpdate.as_view(), name='edit_carrera'),

    path('del_carrera/<int:pk>', views.CarreraDelete.as_view(), name='del_carrera'),

]