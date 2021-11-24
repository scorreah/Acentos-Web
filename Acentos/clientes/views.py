"""Clientes views."""

# Django
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView

from clientes.models import Cliente, Reserva

# Forms
from clientes.forms import SignupForm

# Create your views here.

# def login(request):
#     """Muestra la vista para que se logee el cliente"""
#     return render(request=request,template_name='clientes/login.html')

# class LoginFormView(LoginView):
#     template_name = 'clientes/login.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         return context

def login_view(request):
    """Login view."""
    if request.user.is_authenticated:
        return redirect('clientes:perfil')
    if request.method == 'POST':
        username = request.POST['username']
        passwd = request.POST['password']
        user = authenticate(request, username=username, password=passwd)
        if user:
            login(request, user)
            return redirect('novedades:home')
        else:
            return render(request, 'clientes/login.html', {'error': 'Invalid username and password'})
    return render(request, 'clientes/login.html')

def signup(request):
    """Sign up view."""
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('clientes:login')
    else:
        form = SignupForm()

    return render(
        request=request, 
        template_name='clientes/signup.html',
        context={
            'form': form
        }
    )

def logout_view(request):
    """Logout a user."""
    if request.user.is_authenticated:
        print("Estaba autenticado")
        logout(request)
    return redirect('novedades:home')
    

def perfil(request):
    if request.user.is_authenticated:
        user = request.user
        cliente = Cliente.objects.get(user__exact=user)
        if request.method == 'POST':
            telefono = request.POST['telefono']
            direccion = request.POST['direccion']
            cliente.telefono = telefono
            cliente.direccion = direccion
            cliente.save()
        return render(
            request=request,
            template_name='clientes/perfil.html',
            context={
                'user': user,
                'cliente': cliente
            }
            )
    else:
        return redirect('clientes:login')



def solicitudReserva(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            userInstance = request.user
            user = Cliente.objects.get(user__exact=userInstance)
            titulo = request.POST['titulo']
            autor = request.POST['autor']
            isbn = request.POST['isbn']
            nuevaReserva = Reserva.objects.create(cliente_id=user, autor=autor, ISBN=isbn, titulo=titulo)
            nuevaReserva.save()

        return render(
            request=request,
            template_name='clientes/solicitudReserva.html',
            context={
            }
            )
    else:
        return redirect('clientes:login')