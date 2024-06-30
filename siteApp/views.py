from django.shortcuts import render, redirect
from .models import Pessoa
from .forms import PessoaForm


# Create your views here.

def home(request):
    context = {
        'pessoas': Pessoa.objects.all()
    }
    return render(request, 'content/home.html', context)


def add_pessoa(request):
    form = PessoaForm()
    if request.method == 'POST':
        form = PessoaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('app:home')
    return render(request, 'content/add.html', {'form': form})
