# relatorios/views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import Atividade, Relatorio
from .forms import AtividadeForm, RelatorioForm

def home(request):
    return render(request, 'relatorios/home.html')

def atividades(request):
    if request.user.is_authenticated:
        qs = Atividade.objects.filter(usuario=request.user).order_by('-data_inicio')
    else:
        qs = Atividade.objects.none()
    return render(request, 'relatorios/atividades.html', {'atividades': qs})

def atividade_nova(request):
    if request.method == 'GET':
        form = AtividadeForm()
    else:
        # POST
        if not request.user.is_authenticated:
            return redirect('relatorios:home')

        form = AtividadeForm(request.POST)
        if form.is_valid():
            ativ = form.save(commit=False)
            ativ.usuario = request.user
            ativ.status  = 'ATIVA'
            ativ.save()
            return redirect('relatorios:atividades')

    return render(request, 'relatorios/atividade_form.html', {'form': form})

def relatorios(request):
    return render(request, 'relatorios/relatorios.html')

def validar_relatorio(request, id):
    rel = get_object_or_404(Relatorio, pk=id)
    if request.method == 'POST':
        rel.validado = True
        rel.save()
        return redirect('relatorios:relatorios')
    return render(request, 'relatorios/validacao.html', {'relatorio': rel})

def enviar_relatorio(request, tipo):
    # Exibe a página de envio (formulário) e processa o POST
    if not request.user.is_authenticated:
        return redirect('relatorios:home')

    atividades_user = Atividade.objects.filter(usuario=request.user)

    if request.method == 'POST':
        form = RelatorioForm(request.POST, request.FILES)
        form.fields['atividade'].queryset = atividades_user
        if form.is_valid():
            rel = form.save(commit=False)
            rel.save()
            return redirect('relatorios:relatorios')
    else:
        form = RelatorioForm()
        form.fields['atividade'].queryset = atividades_user

    return render(request, 'relatorios/relatorio_form.html', {
        'form': form,
        'tipo': tipo.capitalize()
    })

def listar_relatorios(request, tipo):
    # Lista todos os relatórios existentes para o tipo selecionado
    if not request.user.is_authenticated:
        return redirect('relatorios:home')

    relatorios = Relatorio.objects.filter(atividade__tipo=tipo)
    return render(request, 'relatorios/listar_relatorios.html', {
        'relatorios': relatorios,
        'tipo': tipo.capitalize(),
    })
