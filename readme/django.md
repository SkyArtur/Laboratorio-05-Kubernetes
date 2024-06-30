# Aplicação Django

### Iniciando o projeto
Em um diretório raiz nomeado como *app_django* executar os comandos a seguir:

- Criando um ambiente virtual: 
    > Windows - `` python -m venv venv ``
    
    > Linux - `` python3 -m venv venv ``

- Iniciando ambiente virtual: 
    > Windows - `` .\venv\Scripts\activate.ps1 ``

    > Linux - `` source venv/bin/activate ``

- Atualizando PIP: 
    > Windows - `` python -m pip install --upgrade pip ``

    > Linux - `` python3 -m pip install --upgrade pip ``

- Instalando dependências: 
    > `` pip install django psycopg2 psycopg2-binary gunicorn ``

- Criando o projeto django: 
    > `` django-admin startproject siteSetup . ``

- Criando a aplicação Django: 
    > Windows - `` python manage.py startapp siteApp ``

    > Linux - `` python3 manage.py startapp siteApp ``

### Trabalhando a aplicação em *./siteApp*
- Editando *models.py*:
```python
from django.db import models


# Create your models here.
class Pessoa(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome')
    sobrenome = models.CharField(max_length=100, verbose_name='Sobrenome')
    nascimento = models.DateField(verbose_name='Nascimento')

    class Meta:
        verbose_name = 'Pessoa'
        verbose_name_plural = 'Pessoas'
        ordering = ['nome', 'sobrenome', 'nascimento']
        unique_together = (('nome', 'sobrenome'),)

    def __str__(self):
        return f'{self.nome} {self.sobrenome}'
```
- Editando *admin.py*:
```python
from django.contrib import admin
from .models import Pessoa

# Register your models here.
admin.site.register(Pessoa)
```

- Criando e editando *forms.py*
```python
from django import forms
from .models import Pessoa


class PessoaForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = '__all__'
```
- Editando *views.py*:
```python
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
```
- Criando e editando *urls.py*:
```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_pessoa, name='add'),
]
```
### Criando arquivos de estilo em *./siteApp/static/css/* 
- Criando e editando *_root.css*:
```css
:root {
    --shadow: inset 0 0 5px 3px rgba(0, 0, 0, 0.10);
    --shadow-out: 0 0 5px 3px rgba(0, 0, 0, 0.10);
    --border: 1px solid rgba(0, 0, 0, 0.10);
    --gradient: linear-gradient(180deg, rgba(2,0,36,1) 0%, rgba(9,9,121,1) 32%, rgba(0,212,255,1) 100%);
    --color-dark: rgb(40, 40, 45);
}
*,*::before, *::after {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: "Segoe UI", system-ui, sans-serif;
}
```
- Criando e editando *_link.css*:
```css
[app-link] {
    display: flex;
    justify-content: center;
    align-items: center;
    cursor: pointer;
}
```
- Criando e editando *_body.css*:
```css
[app-body] {
    width: 100vw;
    height: 100vh;
    background-image: var(--gradient);
    display: grid;
    grid-template-columns: 1fr;
    grid-template-rows: 65px 1fr;
    grid-template-areas: 'header' 'container';
}
```
- Criando e editando *_header.css*:
```css
[app-header] {
    grid-area: header;
    color: aliceblue;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    background-color: var(--color-dark);
}

[app-header] h1 {
    font-size: 1.5rem;
}

[app-header] p {
    font-size: 0.9rem;
}
```
- Criando e editando *_container.css*:
```css
[app-container] {
    grid-area: container;
    background-color: rgb(255, 255, 255);
    margin: 0 auto;
    width: 100%;
    max-width: 1366px;
    min-width: 350px;
    max-height: calc(100vh - 65px);
    display: grid;
    grid-template-columns: 1fr;
    grid-template-rows: 40px 1fr 40px;
    grid-template-areas: 'menu' 'content' 'footer';
}
```
- Criando e editando *_menu.css*:
```css
[app-menu] {
    grid-area: menu;
    display: flex;
    justify-content: center;
    align-items: center;
    max-height: 40px;
    overflow: hidden;
}

[app-nav] {
    display: grid;
    gap: 5px;
    grid-template-rows: 40px;
    grid-template-columns: repeat(2, 150px);
}



[app-nav] [app-link]:hover {
    background-color: var(--color-dark);
    color: white;
}
```
- Criando e editando *_footer.css*:
```css
[app-footer] {
    padding-right: 15px;
    display: flex;
    justify-content: end;
    align-items: center;
}
```
- Criando e editando *_content.css*:
```css
[app-content] {
    margin: 0 10px 5px 10px;
    padding: 15px;
    max-height: calc(100% - 20px);
    box-shadow: var(--shadow);
    overflow-y: auto;
}
```
- Criando e editando *_table.css*:
```css
[app-table] {
    width: 100%;
    border-collapse: collapse;
    text-align: center;
    line-height: 35px;
}

[app-table] thead {
    background-color: var(--color-dark);
    color: white;
}

[app-table] > tbody tr:nth-of-type(even) {
    background-color: aliceblue;
}

[app-table] tr > td:first-child {
    font-weight: bold;
}
```
- Criando e editando *_form.css*:
```css
[app-form] {
    border: var(--border);
    border-radius: 5px;
    height: 430px;
}
[app-form] form {
    padding: 15px;
    display: grid;
    grid-template-columns: 1fr;
    grid-template-rows: repeat(4, 100px);
}

.app-form-control {
    display: flex;
    gap: 5px;
    flex-direction: column;
}

.app-form-control input {
    height: 40px;
    font-size: 20px;
    border: var(--border);
    border-radius: 5px;
    padding-left: 10px;
}

[app-form] .app-form-control:nth-child(4) {
    width: 350px;
}

.app-form-submit {
    display: flex;
    justify-content: center;
    align-items: center;
}

.app-form-submit input {
    height: 50px;
    width: 250px;
    border: var(--border);
    border-radius: 5px;
    background-color: transparent;
    font-size: 1rem;
    box-shadow: var(--shadow-out);
}
.app-form-submit input:hover {
    font-size: 1.2rem;
}

.app-form-submit input:active {
    box-shadow: none;
}
```
- Criando e editando *style.css*:
```css
@import "_root.css";
@import "_link.css";
@import "_body.css";
@import "_header.css";
@import "_container.css";
@import "_menu.css";
@import "_footer.css";
@import "_content.css";
@import "_table.css";
@import "_form.css";
```

