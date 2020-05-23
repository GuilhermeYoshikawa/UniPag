import datetime

from django.shortcuts import render, redirect, get_object_or_404
from .forms import ClienteForm, ConsumidorForm
from .models import Pedido, Produto, Cliente, Consumidor


# Estalogado() é um decorator. verifica se possui um ID na session se sim executa a view q chamou senao chama a view
# login
def estalogado(myview):
    def inner(request, id):  # trocar id por args **
        id_session = request.session['logado']
        if id:
            print(id_session)  # mostra no terminal o id de quem esta logado
            if not id:
                return myview(request)
            else:
                return myview(request, id)
        return loginview(request)

    return inner


def loginview(request):
    # Gambiarra para o search do homecliente nao retornar para o login
    search = request.GET.get('search')
    if search:
        return homeCliente(request)

    # Defini logado False e aplica os metodos de login
    logado = request.session['logado'] = 0
    context = {'logado': logado}  # tive q fazer essas 2 linhas senao aparecia como logado na pagina de login
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']
        user = False
        print(email, senha)

        # print(user.query) mostra a query sql que eh gerado no filter(Ver view logar)
        # tenta logar como cliente
        try:
            user = logarcliente(email, senha)
        except:  # Caso nao seja cliente ira tentar logar como consumidor
            try:
                user = logarconsumidor(email, senha)
            except Exception as e:
                print(e)

        # Apos validar o user ira recirecionalo usando a view redireciona
        if user:
            return redireciona(request, user)

    return render(request, 'login.html', context)  # Se der errado volta para a page de login


# Desloga um user simplesmente settando o ID na session para 0
def logoutview(request):
    request.session['logado'] = 0
    return index(request)


def logarcliente(email, senha):
    cliente = Cliente.objects.filter(email=email, senha=senha)
    return cliente[0]


def logarconsumidor(email, senha):
    consumidor = Consumidor.objects.filter(email=email, senha=senha)
    return consumidor[0]


# Essa view é chamado pelo login. Verifica se quem esta logando é Cliente/Consumidor e redireciona para a view de acordo
def redireciona(request, user):
    context = {'user': user}
    if str(type(user)) == "<class 'unipag.models.Cliente'>":  # Pega a classe do obj user e verifica se é cliente
        request.session[
            'logado'] = user.id_cliente
        return homeCliente(request)

    elif str(type(user)) == "<class 'unipag.models.Consumidor'>":
        request.session['logado'] = user.id_consumidor
        return render(request, 'homeConsumidor.html', context)
    return redirect('login/')


def index(request):
    try:
        logado = request.session['logado']
        context = {'logado': logado}
    except:
        context = {}
        pass

    return render(request, "index.html", context)


def cadastroCliente(request):
    form = ClienteForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('login/')

    return render(request, 'cadastroCliente.html', {'form': form})


def cadastroConsumidor(request):
    form = ConsumidorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('login/')

    return render(request, 'cadastroConsumidor.html', {'form': form})


def homeCliente(request):
    search = request.GET.get('search')
    id = request.session['logado']

    if search:
        pedidos = Pedido.objects.filter(data_pedido__icontains=search)

    else:
        pedidos = Pedido.objects.filter(cliente_id_cliente=id)

    return render(request, "homeCliente.html", {'pedidos': pedidos})


def homeConsumidor(request):
    search = request.GET.get('search')
    id = request.session['logado']

    if search:
        pedidos = Pedido.objects.filter(data_pedido__icontains=search)

    else:
        pedidos = Pedido.objects.filter(consumidor_id_consumidor=id)

    return render(request, "homeConsumidor.html", {'pedidos': pedidos})


def perfilCliente(request):
    id = request.session['logado']
    # cliente = get_object_or_404(Cliente, pk=1)
    cliente = carrega_cliente(id)
    context = prepara_cliente_context(cliente)
    return render(request, "perfilCliente.html", context)


def perfilConsumidor(request):
    id = request.session['logado']
    # cliente = get_object_or_404(Cliente, pk=1)
    consumidor = carrega_consumidor(id)
    context = prepara_consumidor_context(consumidor)
    return render(request, "perfilConsumidor.html", context)


# Semelhante ao de login. Esse metodo carrega usuarios pelo id
def carrega_cliente(id):
    cliente = Cliente.objects.filter(id_cliente=id)
    return cliente[0]


def carrega_consumidor(id):
    consumidor = Consumidor.objects.filter(id_consumidor=id)
    return consumidor[0]


# Recebe um obj cliente e prepara uma context com os dados dele
def prepara_cliente_context(cliente):
    context = {
        'razao_social': cliente.razao_social,
        'cnpj': cliente.cnpj,
        'email': cliente.email,
        'telefone': cliente.telefone,
        'senha': cliente.senha,
        'logadouro': cliente.logradouro,
        'numero': cliente.numero,
        'bairro': cliente.bairro,
        'cep': cliente.cep,
        'cidade': cliente.cidade,
        'uf': cliente.uf,
        'complemento': cliente.complemento,
    }
    return context


def prepara_consumidor_context(consumidor):
    context = {
        'nome': consumidor.nome,
        'sobrenome': consumidor.sobrenome,
        'email': consumidor.email,
        'senha': consumidor.senha,
        'cpf': consumidor.cpf,
        'nascimento': consumidor.nascimento,
        'sexo': consumidor.sexo,
        'logradouro': consumidor.logradouro,
        'numero': consumidor.numero,
        'bairro': consumidor.bairro,
        'cep': consumidor.cep,
        'cidade': consumidor.cidade,
        'uf': consumidor.uf,
        'complemento': consumidor.complemento,
        'telefone': consumidor.telefone,
        'nacionalidade': consumidor.nacionalidade,
        'numero_cartao': consumidor.numero_cartao,
        'codigo_seguranca': consumidor.codigo_seguranca,
        'titular_cartao': consumidor.titular_cartao,
        'validade_cartao': consumidor.validade_cartao,
        'limite_compra': consumidor.limite_compra,
    }
    return context


def editarCliente(request):
    id = request.session['logado']
    cliente = get_object_or_404(Cliente, pk=id)
    form = ClienteForm(request.POST or None, instance=cliente)
    if form.is_valid():
        form.save()
        return redirect('homeCliente')

    return render(request, "editarCliente.html", {'cliente': cliente, 'form': form})


def editarConsumidor(request):
    id = request.session['logado']
    consumidor = get_object_or_404(Consumidor, pk=id)
    form = ConsumidorForm(request.POST or None, instance=consumidor)
    if form.is_valid():
        form.save()
        return redirect('homeConsumidor')

    return render(request, "editarConsumidor.html", {'consumidor': consumidor, 'form': form})


def produtoView(request, id):
    produto = get_object_or_404(Produto, pk=id)
    return render(request, 'produto.html', {'produto': produto})


@estalogado
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
