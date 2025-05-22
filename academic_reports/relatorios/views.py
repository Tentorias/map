from django.shortcuts import render, get_object_or_404, redirect
from .models import Atividade, Relatorio
from .forms import AtividadeForm

def home(request):
    return render(request, 'relatorios/home.html')


def atividades(request):
    if request.user.is_authenticated:
        qs = Atividade.objects.filter(usuario=request.user).order_by('-data_inicio')
    else:
        qs = Atividade.objects.none()   #
    return render(request, 'relatorios/atividades.html', {'atividades': qs})

def atividade_nova(request):
    # Se for GET, apenas exibe o form
    if request.method == 'GET':
        form = AtividadeForm()
        return render(request, 'relatorios/atividade_form.html', {'form': form})

    # === Se chegou aqui, é POST ===
    # Bloqueia anônimos ao tentar submeter
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

def visualizar_relatorio(request, tipo):
    return render(request, 'relatorios/relatorio_form.html', {'tipo': tipo})
