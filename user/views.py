from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .forms import *
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

# Create your views here.

def userRegister(request):

    form = UserForm()

    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            subject = "Başarılı Kayıt"
            message = f"Kullanıcı kaydı başarıyla oluşturuldu"

            
            send_mail(
                subject,
                message,
                settings.EMAIL_HOST_USER,
                [form.email],
            )
            

            form.save()
            return redirect('login')
        
    context = {
        'form':form
    }

    return render(request, "register.html", context)

def userLogin(request):

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            messages.success(request, "Başarıyla giriş yapıldı!")
            return redirect("index")
        else:
            messages.error(request, "Kullanıcı adı ya da şifre yanlış!")
            return redirect("login")

    return render(request, "login.html")

def userLogout(request):
    logout(request)
    messages.success(request, "Başarılı bir şekilde oturumunuz kapatıldı.")
    return redirect('index')


def passwordChange(request):

    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, request.user)
            logout(request)
            messages.success(request, "Şifre değiştirme işlemi başarılı..")
            return redirect('login')
        else:
            messages.error(request, "Giriğiniz bilgiler hatalı...")
    else:
        form = PasswordChangeForm(request.user)

    context = {
        'form':form
    }

    return render(request, "password_change.html",context)

def account_delete(request):

    user = request.user

    if request.method == "POST":
        if user.is_authenticated:
            user = request.user
            user.delete()
            logout(request)
            messages.success(request, "Hesabınız başarıyla silindi...")
            return redirect('index')
        
        else:
            messages.error(request, "Hesabı silmek için girişli olmalısın!")
            return redirect('login')

    return render(request, "account_delete.html")