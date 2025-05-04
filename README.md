# Curso de Desarrollo Web con Flask + Proyecto To-Do List

## Descripción

Este repositorio forma parte del curso de desarrollo web con **Flask**, el microframework de Python. El objetivo del curso es proporcionar una base sólida para construir aplicaciones web modernas, abordando temas clave como plantillas, formularios, bases de datos, autenticación, APIs REST, despliegue y más.

El curso está estructurado en diez secciones progresivas, culminando en la creación de varios proyectos, incluyendo una aplicación de **To-Do List** completamente funcional.

---

## Contenido del Curso

### 1. Introducción a Flask

- Instalación de dependencias.
- Configuración del entorno virtual.
- Creación de una aplicación básica.
- Ejecución del servidor local.

### 2. Plantillas con Jinja2 y HTML

- Uso del motor de plantillas Jinja2.
- Estructuración de vistas dinámicas con HTML.
- Uso de bloques y herencia de plantillas.

### 3. Manejo de Formularios

- Creación y validación de formularios con Flask.
- Manejo de datos enviados por el usuario.
- Gestión de errores y mensajes flash.

### 4. Estructura de una Aplicación - To-Do List

- Desarrollo de una aplicación de lista de tareas.
- Organización modular del proyecto.
- Enrutamiento de vistas y gestión de tareas.

### 5. Base de Datos - Flask-SQLAlchemy

- Configuración de la base de datos con SQLAlchemy.
- Definición de modelos y relaciones.
- Ejecución de consultas básicas.

### 6. Autenticación de Usuarios

- Registro, inicio y cierre de sesión.
- Gestión de sesiones de usuario.
- Protección de rutas privadas.

### 7. Proyecto BLOG-POSTS

- Creación de publicaciones y comentarios.
- Autenticación en acciones restringidas.
- Estructura CRUD con formularios personalizados.

### 8. API REST con Flask

- Creación de endpoints RESTful.
- Uso de métodos HTTP: GET, POST, PUT, DELETE.
- Formato JSON y pruebas con herramientas externas.

### 9. Proyecto Final - Portafolio

- Desarrollo completo de una aplicación de portafolio.
- Envío de correos desde formularios de contacto.
- Uso de habilidades integradas de todo el curso.

### 10. Despliegue de Aplicaciones

- Preparación de la app para producción.
- Despliegue en servidores (ej. Render, Heroku).
- Configuración de variables de entorno y bases de datos externas.

---

## Proyecto Destacado: To-Do List

El proyecto **To-Do List** es uno de los primeros proyectos prácticos del curso, diseñado para reforzar los conceptos fundamentales de Flask. Incluye:

- Agregar, eliminar y marcar tareas como completadas.
- Uso de rutas dinámicas.
- Base de datos con SQLAlchemy.
- Diseño limpio con plantillas HTML y Jinja2.
- Organización del código en formato modular.

---

## Requisitos

- Python 3.10+
- pip
- Entorno virtual (recomendado)
- Flask
- Flask-SQLAlchemy

---

## Instalación y Ejecución

```bash
# Clona este repositorio
git clone https://github.com/tu_usuario/to-do-list.git
cd to-do-list

# Activa el entorno virtual
python -m venv .venv
source .venv/bin/activate  # En Windows: .venv\Scripts\activate

# Instala las dependencias
pip install -r requirements.txt

# Ejecuta la aplicación
flask --app todor --debug run
