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

## Trabalhando a aplicação em *./siteApp*
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
### Criando arquivo javascript em *./siteApp/static/js/*
- Criando e editando *main.js*
O arquivo em questão será utilizado para programar os links da aplicação.
```javascript
(
    function () {
        let appLink = document.querySelectorAll('[app-link]')
        if (appLink) {
            appLink.forEach(link => {
                const [url, target] = link.getAttribute('app-link').split(' ')
                const location = window.location.pathname
                link.addEventListener('click', () => {
                    window.open(url, target ?? '_self')
                })
                if (location === url) link.style = 'background-color: var(--color-dark); color: white;'
            })
        }
    }
)()
```
## Trabalhando a aplicação em *./siteSetup*
- Editando as configurações padrões do arquivo *settings.py*.
  - INSTALLED APPS 
  ```python
  INSTALLED_APPS = [
      'django.contrib.admin',
      'django.contrib.auth',
      'django.contrib.contenttypes',
      'django.contrib.sessions',
      'django.contrib.messages',
      'django.contrib.staticfiles',
      'siteApp'
  ]
  ```
  - TEMPLATES
  ```python
  TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
  ]
  ```
  - DATABASES
  ```python
  DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.postgresql_psycopg2',
          'NAME': 'laboratorio',
          'USER': 'estudante',
          'PASSWORD': '212223',
          'HOST': 'postgres',
          'PORT': 5432,
      }
  }
  ```
  - LANGUAGE E STATICS
  ```python
  LANGUAGE_CODE = 'pt-br'
  
  TIME_ZONE = 'America/Sao_Paulo'
  
  USE_I18N = True
  
  USE_TZ = True
  
  
  # Static files (CSS, JavaScript, Images)
  # https://docs.djangoproject.com/en/5.0/howto/static-files/
  
  STATIC_URL = 'static/'
  
  STATIC_ROOT = BASE_DIR / 'staticfiles'
  
  STATICFILES_DIRS = [BASE_DIR / 'siteApp/static']
  ```
- editando arquivo *urls.py*
```python
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static, settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('siteApp.urls', 'siteApp'), namespace='app'))
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

```
## Trabalhando a aplicação em *./templates*

Após a criação do diretório *templates*, criar dentro do mesmo os diretórios *includes* e *content* e o arquivo *index.html*.
- criando e editando o arquivo *includes/_header.html*
```html
<header app-header>
    <h1>Aplicação de teste</h1>
    <p>Testando o deploy de uma aplicação Django com Kubernetes</p>
</header>
```
- criando e editando o arquivo *includes/_menu.html*
```html
<aside app-menu>
    <nav app-nav>
        <div app-link="{% url 'app:home' %}">Home</div>
        <div app-link="{% url 'app:add' %}">Cadastrar</div>
    </nav>
</aside>
```
- criando e editando o arquivo *includes/_footer.html*
```html
<footer app-footer>
    <small app-link="https://github.com/SkyArtur _blank">SkyArtur/Development</small>
</footer>
```
- criando e editando o arquivo *content/home.html*
```html
{% extends 'index.html' %}

{% block title %}HOME{% endblock %}

{% block content %}
    <table app-table>
        <thead>
            <tr>
                <th>NOME</th>
                <th>SOBRENOME</th>
                <th>NASCIMENTO</th>
            </tr>
        </thead>
        <tbody>
            {% for pessoa in pessoas %}
            <tr>
                <td>{{ pessoa.nome }}</td>
                <td>{{ pessoa.sobrenome }}</td>
                <td>{{ pessoa.nascimento|date:'d/m/Y' }}</td>
            </tr>
            {% endfor %}
        </tbody>
    </table>
{% endblock %}
```
- criando e editando o arquivo *content/add.html*
```html
{% extends 'index.html' %}

{% block title %}CADASTRAR{% endblock %}

{% block content %}
	<div app-form>
        <form method="post">
            {% csrf_token %}
            <div class="app-form-control">
                <label>NOME</label>
                {{ form.nome }}
            </div>
            <div class="app-form-control">
                <label>SOBRENOME</label>
                {{ form.sobrenome }}
            </div>
            <div class="app-form-control">
                <label>NASCIMENTO</label>
                {{ form.nascimento }}
            </div>
            <div class="app-form-submit">
                <input type="submit" formaction="{% url 'app:add' %}">
            </div>
        </form>
    </div>
{% endblock %}
```
- criando e editando o arquivo *index.html*
```html
{% load static %}
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Django | {% block title %}{% endblock %}</title>
    <link rel="stylesheet" href="{% static 'css/style.css' %}">
</head>
<body app-body>
    {% include 'includes/_header.html' %}
    <div app-container>
        {% include 'includes/_menu.html' %}
        <div app-content>
            {% block content %}{% endblock %}
        </div>
        {% include 'includes/_footer.html' %}
    </div>
    <script src="{% static 'js/main.js' %}"></script>
</body>
</html>
```
# Conclusão

Para concluir vamos realizar a coleta dos arquivos estáticos e criar o arquivo requirements.txt com os comandos:
> ``python manage.py collectstatic``

> ``pip freeze >> requirements.txt``

Agora que a aplicação está concluída, ela pode ser testada. Como o banco de dados para a aplicação já foi definido, para 
realizar os testes podemos editar a constante ***DATABASES*** para a utilização de um banco de dados sqlite, mas
lembre-se de retornar a configuração anterior antes de criar a imagem da aplicação:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite',
    }
}
```

Realizar as migrações
> ``python manage.py makemigrations``

> ``python manage.py migrate``

Executar a aplicação:
> ``python manage.py runserver``
