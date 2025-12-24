from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from usuarios.forms import LoginForms, CadastroForms

def login(request):
    form = LoginForms()
    return render(request, 'usuarios/login.html', {'form': form})

def cadastro(request):
    form = CadastroForms(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            if form['senha_1'].value() != form['senha_2'].value():
                return redirect('cadastro')
            nome = form['']
            form.save()

    return render(request, 'usuarios/cadastro.html')