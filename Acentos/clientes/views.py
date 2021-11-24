"""Clientes views."""

# Django
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView

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
    
@login_required
def perfil(request):
    user = request.user
    return render(
        request=request,
        template_name='clientes/perfil.html',
        context={
            'user': user
        }
        )