
# To-Do App Backend API

Este es el backend para una aplicación de gestión de tareas (To-Do List), creada con **Django** y **Django REST Framework**. La base de datos está configurada para usar **MongoDB Atlas** mediante el paquete **Djongo**.

## Tabla de Contenidos

1. [Introducción](#introducción)
2. [Tecnologías utilizadas](#tecnologías-utilizadas)
3. [Configuración del entorno](#configuración-del-entorno)
4. [Instalación](#instalación)
5. [Uso](#uso)
6. [Endpoints](#endpoints)

## Introducción

Este proyecto proporciona una API RESTful para gestionar tareas, permitiendo operaciones básicas como crear, leer, actualizar y eliminar tareas. La base de datos MongoDB está configurada a través de Djongo para ser compatible con Django.

## Tecnologías utilizadas

- **Django**: Framework de desarrollo web de alto nivel en Python.
- **Django REST Framework**: Librería para crear APIs en Django.
- **MongoDB Atlas**: Base de datos NoSQL basada en la nube.
- **Djongo**: Paquete que permite usar MongoDB como base de datos en Django.

## Configuración del entorno

Este proyecto utiliza **MongoDB Atlas** como base de datos, y Djongo para integrarlo con Django. Asegúrate de tener acceso a MongoDB Atlas y configura las credenciales adecuadas en el archivo de configuración `settings.py`.

La configuración de la base de datos en `settings.py` es la siguiente:

```python
DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'ToDoList',
        'ENABLED': True,
        'CLIENT': {
            'host': 'mongodb+srv://<username>:<password>@cluster0.mongodb.net/ToDoList?retryWrites=true&w=majority',
            'username': 'yhomi',  # Cambia con tu usuario de MongoDB Atlas
            'password': 'yhomi',  # Cambia con tu contraseña de MongoDB Atlas
            'authSource': 'admin',
            'authMechanism': 'SCRAM-SHA-1'
        }
    }
}
```

### Notas sobre MongoDB Atlas:
- Asegúrate de tener un clúster de MongoDB Atlas configurado.
- Sustituye los valores de `<username>` y `<password>` con tus credenciales reales.

## Instalación

### Requisitos

- **Python 3.x**: Asegúrate de tener Python 3.x instalado en tu sistema.
- **MongoDB Atlas**: Necesitarás una cuenta en MongoDB Atlas y una base de datos configurada.

### Pasos para instalar:

1. Clona este repositorio:

```bash
git clone https://github.com/tu-usuario/to-do-app-backend.git
cd to-do-app-backend
```

2. Crea y activa un entorno virtual:

```bash
python -m venv env
source env/bin/activate  # En Windows usa: env\Scriptsctivate
```

3. Instala las dependencias:

```bash
pip install -r requirements.txt
```

4. Realiza las migraciones de la base de datos:

```bash
python manage.py migrate
```

5. Inicia el servidor:

```bash
python manage.py runserver
```

Tu API debería estar corriendo en `http://127.0.0.1:8000/`.

## Uso

Puedes interactuar con la API mediante herramientas como **Postman** o **cURL**. Aquí se detallan los endpoints disponibles:

### Endpoints:

- `GET /tasks/`: Devuelve todas las tareas.
- `GET /tasks/{id}/`: Devuelve una tarea por su ID.
- `POST /tasks/`: Crea una nueva tarea.
- `PUT /tasks/{id}/`: Actualiza una tarea existente.
- `DELETE /tasks/{id}/`: Elimina una tarea.

### Ejemplo de creación de tarea (POST):

**Request:**

```bash
POST http://127.0.0.1:8000/tasks/
Content-Type: application/json

{
  "title": "Comprar leche",
  "description": "Comprar leche en el supermercado",
  "status": "PENDING"
}
```

**Response:**

```json
{
  "title": "Comprar leche",
  "description": "Comprar leche en el supermercado",
  "status": "PENDING",
  "created_at": "2024-11-28T15:30:00Z",
  "updated_at": "2024-11-28T15:30:00Z",
  "_id": "63d9d8c1d24b2a5dbd48245a"
}
```

