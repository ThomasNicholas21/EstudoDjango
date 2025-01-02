# Django Framework

- Framework para desenvolvimento web de forma rápida, segura e escalável, que segue o padrão MVT (Model-View-Tamplate).

### MVT - Model-View-Control
- **Model:** vai gerarenciar a estrutura lógica de dados, mapeando os dados do manco de forma orientada a objeto.
- **View:** controla o que é exibido no navegador do usuário, manipulanto solicitações HTTP.
- **Template:** Define a apresentação visual dos dados, usando sistemas de templates do Django.

# Arquivos
## __settings.py:__ 
Toda a configuração da aplicação é feita nesse arquivo, definindo váriaveis de ambinete e configurações gerais para o funcionamento do aplicativo, como conexão com banco de dados, localização de templates, e detalhes de segurança.
- Configurações principais:
    - BASE_DIR
    - SECRET_KEY
    - DEBUG
    - ALLOWED HOSTS
- Aplicativos
    - INSTALLED_APPS
- Middlewares
    - MIDDLEWARE
- URLS E WSGI
    - ROOT_URLCONF
    - WSGI_APPLICATION
- Banco de dados
    - DATABASES
- Autentincação
    - AUTH_PASSORD_VALIDATORS
- Internacionalização
- Arquivos estáticos e mídia
    - STATIC_URL
    - MEDIA_URL/MEDIA_ROOT
- Outros
    - TEMPLATES
    - DEFAULT_AUTO_FIELD

# Comandos

### Iniciar projeto
```cmd
> django-admin startproject NomeProjeto
```
```cmd
>django-admin startproject NomeProjeto .
```

### Iniciar servidor
```cmd
>python manage.py runserver
```