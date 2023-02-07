from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.utils.crypto import get_random_string

# Create your views here.
from django.utils import translation

from .forms import SignUpForm, UserUpdateForm, ProfileUpdateForm
from .models import UserProfile,Lista


def Login_Form(request):
    if request.method == 'POST':# si el existe un metodo post
        username = request.POST['username']#tomamos pasword y useername 
        password = request.POST['password']

#------------------AUTHENTICATE--USERS--------------#

        user = authenticate(request, username=username, password=password)#luego lo autnticamos
        if user is not None:# si la var user no esta vacia login

#---------------FUNTION--LOGIN--USERS--------------#

            login(request, user)
            return HttpResponseRedirect('/')
        else:
            messages.warning(request,"Error de validacion !! Username o Password es imcorrecto")
            return HttpResponseRedirect('/login')
    ctx = {
        
    }
    return render(request, 'usuarios/login.html',ctx)
#---------------LOGIN--USERS---END-----------------#
@login_required(login_url='/login')
def Logout_Form(request):
    logout(request)
    return HttpResponseRedirect('/login')

def Signup_Form(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save() #completed sign up
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            # Create data in profile table for user
            current_user = request.user
            data=UserProfile()
            data.user_id=current_user.id
            data.image="icons/icon-header-01.png"
            cuponcode= get_random_string(15).upper()
            data.codigo =  cuponcode
            data.save()
            messages.success(request, 'Tu Cuenta Fue Creada Exitosamente!')
            return HttpResponseRedirect('/')
        else:
            messages.success(request,form.errors)
            return HttpResponseRedirect('/siginup')


    form = SignUpForm()

#------------------------------------------------------CONTEXTO--DE--LA--VISTA--------------------------------------------------------#

    context = {
               'form': form,
    }
    return render(request, 'usuarios/registro.html', context)

@login_required(login_url='/Login') # Check login
def Update_Form(request):

#-----------------------------------------------------VALIDACION--DE--USUARIOS----------------------------------------------------------#

    current_user = request.user
    profile = UserProfile.objects.get(user_id=current_user.id)

#-----------------------------------------------------VALIDACION--DE--USUARIOS--END--------------------------------------------------------#
    
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user) # request.user is user  data
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your account has been updated!')
            return HttpResponseRedirect('/Usuarios/perfil')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.userprofile) #"userprofile" model -> OneToOneField relatinon with user
        context = {
            'user_form': user_form,
            'profile_form': profile_form
        }

#------------------------------------------------------CONTEXTO--DE--LA--VISTA--------------------------------------------------------#

        return render(request, 'usuarios/usuarios/completar_formulario.html', context)

@login_required(login_url='/Login')
def Perfil_User(request):

    current_user = request.user
    profile = UserProfile.objects.get(user_id=current_user.id)
    lista = Lista.objects.filter(user_id=current_user.id)
    numero=0
    for rs in lista:
        numero += 1 * 1
    if profile:
        ctx = {
        'profile':profile,
        'lista':lista,
        'numero':numero,
        }
    else:
        ctx = {
        'numero':numero,
        'lista':lista
        }
    
    return render(request, 'usuarios/usuarios/index.html',ctx)

@login_required(login_url='/Login')
def Agregra_Lista(request,id):

    url = request.META.get('HTTP_REFERER')
    current_user = request.user
    data = Lista()
    data.ip = request.META.get('REMOTE_ADDR')
    data.user_id = current_user.id
    data.pelicula_id = id
    data.save()

    return HttpResponseRedirect(url)

@login_required(login_url='/Login')
def Quitar_Lista(request,id):
    url = request.META.get('HTTP_REFERER')
    Lista.objects.filter(pelicula_id=id).delete()
    return HttpResponseRedirect(url)