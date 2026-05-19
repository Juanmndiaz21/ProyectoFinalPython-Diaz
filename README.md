# Proyecto Final - Blog en Django

Aplicación web estilo blog desarrollada en **Python + Django** con autenticación, perfiles, mensajería y gestión de páginas.

## Funcionalidades principales
- Registro, login y logout
- Perfil de usuario con edición y cambio de contraseña
- Blog/Páginas con CRUD completo
- Vista de detalle y listado de páginas
- Mensajería entre usuarios
- Vista **About**
- Panel de admin

## Requisitos
- Python 3.10+ (recomendado)
- pip
- Virtualenv (opcional)

## Instalación
```bash
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

## Migraciones y superusuario
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

## Ejecución
```bash
python manage.py runserver
```

Abrir en el navegador:  
`http://127.0.0.1:8000/`

## Rutas principales
- `/` → Home  
- `/about/` → About  
- `/pages/` → Listado de páginas  
- `/pages/<id>/` → Detalle  
- `/accounts/login/` → Login  
- `/accounts/signup/` → Registro  
- `/accounts/profile/` → Perfil  
- `/messages/` → Bandeja de mensajes  

## Admin
`/admin/` con el usuario creado por `createsuperuser`.

## Video demo
https://youtu.be/vE_I8YnqbX0
