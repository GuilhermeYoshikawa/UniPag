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
    path('meuPerfil/', views.meuPerfil, name='meuPerfil'),
    path('editarCliente/', views.editarCliente, name='editarCliente'),
    path('editarConsumidor/', views.editarConsumidor, name='editarConsumidor'),
    path('logout/', views.logoutview, name='logoutview'),
    path('preparaCompra/', views.preparaCompra_verificalogado, name='PreparaCompra_verificalogado'),
    path('compraCredito/', views.compraCredito, name='compraCredito'),
    path('GeneratePDF/', views.GeneratePDF, name='GeneratePDF')
]
