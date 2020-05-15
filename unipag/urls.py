from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.loginview, name='loginview'),
    path('cadastroCliente/', views.cadastroCliente, name='cadastroCliente'),
    path('home/', views.homeCliente, name='homeCliente'),
    path('pedido/<int:id>', views.pedidoView, name='pedidoView'),
    path('relatorio/', views.relatorio, name='relatorio'),
    path('meuPerfil/<int:id>', views.perfilCliente, name='perfilCliente'),
    path('editarCliente/<int:id>', views.editarCliente, name='editarCliente'),
    path('cadastroConsumidor/', views.cadastroConsumidor, name='cadastroConsumidor'),
    path('homeConsumidor/', views.homeConsumidor, name='homeConsumidor'),
    path('produto/<int:id>', views.produtoView, name='produtoView'),
]