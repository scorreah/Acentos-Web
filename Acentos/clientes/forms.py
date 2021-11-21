"""Clientes forms."""

# Django
from django import forms
from django.forms.widgets import TextInput

# Models
from usuarios.models import User
from clientes.models import Cliente, Carrito


class SignupForm(forms.Form):
    "Signup form."
    # Usuario
    username = forms.CharField(min_length=4, max_length=50, widget=TextInput(
        attrs={'class': 'form-control', 'placeholder':'Ingrese un nombre de usuario...'}))

    email = forms.CharField(required=True, widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder':'Ingrese su correo electronico...'}))

    password = forms.CharField(max_length=70, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder':'Ingrese una contraseña...'}))
    password_confirmation = forms.CharField(max_length=70, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder':'Ingrese nuevamente la contraseña...'}))

    # Cliente

    # Validaciones
    # Validación especifica
    def clean_username(self):
        """Username must be unique."""
        # Los datos que ya limpio django por nosotros
        username = self.cleaned_data['username']
        # Usamos filter porque si usamos get y no existe, lanzaría una excepción
        # exist() solo para saber si existe (booleano)
        username_taken = User.objects.filter(username=username).exists() 
        if username_taken:
            # Django se encarga de subir la excepción hasta el html
            raise forms.ValidationError('El nombre de usuario no se encuentra disponible.')
        return username # Es necesario que cuando se haga la validación de un campo, se regrese el campo

    # Validación especifica
    def clean_email(self):
        """Email must be unique."""
        # Los datos que ya limpio django por nosotros
        email = self.cleaned_data['email']
        # Usamos filter porque si usamos get y no existe, lanzaría una excepción
        # exist() solo para saber si existe (booleano)
        email_taken = User.objects.filter(email=email).exists() 
        if email_taken:
            # Django se encarga de subir la excepción hasta el html
            raise forms.ValidationError('El email ya está en uso.')
        return email # Es necesario que cuando se haga la validación de un campo, se regrese el campo
    
    # Validación final de todos los datos
    def clean(self):
        """Verify password confirmation match."""
        # Para no sobreescribir todo el metodo
        data = super().clean()

        password = data['password']
        password_confirmation = data['password_confirmation']

        if password != password_confirmation:
            raise forms.ValidationError('¡Las contraseñas no coinciden!')

        return data

    def save(self):
        """Crea un usuario."""
        data = self.cleaned_data
        # Hay un dato que no nos sirve, que es password confirmation
        data.pop('password_confirmation')
        usuario = {
            'username': data['username'],
            'email': data['email'],
            'usuario_cliente': True,
        }
        # Le enviamos todo el formulario

        user = User.objects.create(**usuario)
        print("Sin problemas")
        user.set_password(data['password'])
        user.save()
        carrito = Carrito.objects.create(precio=0)
        carrito.save()
        cliente = Cliente.objects.create(user=user, carrito=carrito)
        cliente.save()
