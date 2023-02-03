from django.urls import path
from AppProyectoFinal import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.inicio, name="inicio"), #esta era nuestra primer view
    path('Politica', views.politica, name="Politica"),
    path('Sociedad', views.sociedad, name="Sociedad"),
    path('Deporte', views.deporte, name="Deporte"),
    path('Internacional', views.internacional, name="Internacional"),
    path('login', views.login_request, name="Login"),
    path('logout', LogoutView.as_view(template_name='AppProyectoFinal/logout.html'), name='Logout'),
    path('register', views.register, name='Register'),
    path('editarPerfil', views.editarPerfil, name="EditarPerfil"),
    path('sociedad/list', views.SociedadList.as_view(), name='List'),
    path(r'^(?P<pk>\d+)$', views.SociedadDetalle.as_view(), name='Detail'),
    path(r'^nuevo$', views.SociedadCreacion.as_view(), name='New'),
    path(r'^editar/(?P<pk>\d+)$', views.SociedadUpdate.as_view(), name='Edit'),
    path(r'^borrar/(?P<pk>\d+)$', views.SociedadDelete.as_view(), name='Delete'),
    path('buscar', views.buscar, name='Buscar'),
    path('nosotros', views.nosotros, name='Nosotros'),
    path('nada', views.nada, name='Nada')
]
