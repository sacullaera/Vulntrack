from django.shortcuts import render, redirect
from .forms import AtivoFisicoModelForm, EmpresaModelForm, FuncionarioModelForm, AtivoLogicoModelForm
from django.contrib import messages


def cadastro_empresa(request):
    if str(request.method) == 'POST':
        form = EmpresaModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Empresa cadastrada com sucesso!')
            return render(request, 'empresa.html', {'form': EmpresaModelForm()})  # Substitua 'empresa.html' pelo nome da URL ou caminho correto
    else:
        form = EmpresaModelForm()
    
    return render(request, 'empresa.html', {'form': form})

def cadastro_funcionario(request):
    if str(request.method) == 'POST':
        form = FuncionarioModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Funcionário cadastrado com sucesso!')
            return render(request, 'funcionario.html', {'form': FuncionarioModelForm()})  # Substitua 'funcionario.html' pelo nome da URL ou caminho correto
    else:
        form = FuncionarioModelForm()
    
    return render(request, 'funcionario.html', {'form': form})

def cadastro_ativo_logico(request):
    if str(request.method) == 'POST':
        form = AtivoLogicoModelForm(request.POST)
        if form.is_valid():
            novo_ativo = form.save()
            tipo_ativo = 'logico'
            messages.success(request, 'Ativo lógico cadastrado com sucesso!')
            return render(request, 'ativoLogico.html', {'form': form})  
    else:
        form = AtivoLogicoModelForm()
    
    return render(request, 'ativoLogico.html', {'form': form})

def cadastro_ativo_fisico(request):
    if str(request.method) == 'POST':
        form = AtivoFisicoModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            tipo_ativo = 'fisico'
            messages.success(request, 'Ativo físico cadastrado com sucesso!')
            return render(request, 'ativoFisico.html', {'form': form})  
    else:
        form = AtivoFisicoModelForm()
    
    return render(request, 'ativoFisico.html', {'form': form})