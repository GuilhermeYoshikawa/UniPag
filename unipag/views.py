import datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ClienteForm, ConsumidorForm
from .models import Pedido, Produto, Cliente, Consumidor


# Create your views here.

def loginview(request):
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']
        user = False
        print(email, senha)

        # tenta logar como cliente
        # user = Cliente.objects.filter(email=email)#.values_list('id_cliente', flat=True)
        # print(user.query)
        try:
            user = logarcliente(email, senha)
        except:
            try:
                user = logarconsumidor(email, senha)
            except Exception as e:
                print(e)

        # tentara logar como consumidor caso nao retorne nada do logar como cliente

        if user:
            return redireciona(request, user)

    return render(request, 'login.html')


def logarcliente(email, senha):
    cliente = Cliente.objects.filter(email=email, senha=senha)
    return cliente[0]


def logarconsumidor(email, senha):
    consumidor = Consumidor.objects.filter(email=email, senha=senha)
    return consumidor[0]


def redireciona(request, user):
    context = {'user': user}
    if str(type(user)) == "<class 'unipag.models.Cliente'>":
        return render(request, 'homeCliente.html', context)

    elif str(type(user)) == "<class 'unipag.models.Consumidor'>":
        return render(request, 'homeConsumidor.html', context)
    return redirect('login/')


def index(request):
    context = {}
    return render(request, "index.html", context)


def cadastroCliente(request):
    form = ClienteForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('login/')

    return render(request, 'cadastroCliente.html', {'form': form})


def homeCliente(request):
    search = request.GET.get('search')

    if search:
        pedidos = Pedido.objects.filter(data_pedido__icontains=search)

    else:
        pedidos = Pedido.objects.all()

    return render(request, "homeCliente.html", {'pedidos': pedidos})


def perfilCliente(request, id):
    cliente = get_object_or_404(Cliente, pk=1)
    return render(request, "perfilCliente.html", {'cliente': cliente})


def editarCliente(request, id):
    cliente = get_object_or_404(Cliente, pk=1)
    form = ClienteForm(request.POST or None, instance=cliente)
    if form.is_valid():
        form.save()
        return redirect('homeCliente')

    return render(request, "editarCliente.html", {'cliente': cliente, 'form': form})


def cadastroConsumidor(request):
    form = ConsumidorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('login/')

    return render(request, 'cadastroConsumidor.html', {'form': form})


def homeConsumidor(request):
    search = request.GET.get('search')

    if search:
        produtos = Produto.objects.filter(nome__icontains=search)

    else:
        produtos = Produto.objects.all()

    return render(request, "homeConsumidor.html", {'produtos': produtos})


def produtoView(request, id):
    produto = get_object_or_404(Produto, pk=id)
    return render(request, 'produto.html', {'produto': produto})


def pedidoView(request, id):
    pedido = get_object_or_404(Pedido, pk=id)
    produto = get_object_or_404(Produto, pk=id)
    return render(request, 'pedido.html', {'pedido': pedido, 'produto': produto})


def relatorio(request):
    recentes = Pedido.objects.filter(status_pedido='Concluído',
                                     data_pedido=datetime.datetime.now() - datetime.timedelta(days=30),
                                     id_cliente=1).count()
    concluida = Pedido.objects.filter(status_pedido='Concluído', id_cliente=1).count()
    andamento = Pedido.objects.filter(status_pedido='Em andamento', id_cliente=1).count()

    return render(request, "relatorio.html", {'recentes': recentes, 'concluida': concluida, 'andamento': andamento})
