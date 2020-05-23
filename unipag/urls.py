from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.loginview, name='loginview'),
    path('cadastroCliente/', views.cadastroCliente, name='cadastroCliente'),
    path('cadastroConsumidor/', views.cadastroConsumidor, name='cadastroConsumidor'),
    path('home/', views.homeCliente, name='homeCliente'),
    path('homeConsumidor/', views.homeConsumidor, name='homeConsumidor'),
    path('pedido/<int:id>', views.pedidoView, name='pedidoView'),
    path('relatorio/', views.relatorio, name='relatorio'),
    path('meuPerfilCliente/', views.perfilCliente, name='perfilCliente'),
    path('meuPerfilConsumidor/', views.perfilConsumidor, name='perfilConsumidor'),
    path('editarCliente/', views.editarCliente, name='editarCliente'),
    path('editarConsumidor/', views.editarConsumidor, name='editarConsumidor'),
    path('produto/<int:id>', views.produtoView, name='produtoView'),
    path('logout/', views.logoutview, name='logoutview'),
]
