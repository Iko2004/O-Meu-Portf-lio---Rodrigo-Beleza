from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegistoForm

def login_view(request):
    if request.method == "POST":
        user = authenticate(
            request, 
            username=request.POST.get('username'), 
            password=request.POST.get('password')
        )
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Utilizador ou password inválidos.")
    
    return render(request, 'accounts/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def registo_view(request):
    form = RegistoForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, "Conta criada com sucesso! Faça login.")
            return redirect('login')
    
    return render(request, 'accounts/registo.html', {'form': form})