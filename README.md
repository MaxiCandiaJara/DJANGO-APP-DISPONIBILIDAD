

# DJANGO-APP-DISPONIBILIDAD

Aplicación web desarrollada con **Django** y **HTML** para gestionar la disponibilidad de hermanos de la organizacion JW.

## Características principales

- Backend en Python usando el framework Django.
- Interfaz de usuario diseñada con HTML.
- Gestión de disponibilidad y horarios.
- Fácil de instalar y desplegar.

## Requisitos

- Python 3.8 o superior
- Django 3.x o superior

## Instalación

1. Clona el repositorio:
    ```bash
    git clone https://github.com/MaxiCandiaJara/DJANGO-APP-DISPONIBILIDAD.git
    ```
2. Entra al directorio del proyecto:
    ```bash
    cd DJANGO-APP-DISPONIBILIDAD
    ```
3. Crea y activa un entorno virtual:
    ```bash
    python -m venv venv
    source venv/bin/activate  # En Windows: venv\Scripts\activate
    ```
4. Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    ```
5. Aplica las migraciones:
    ```bash
    python manage.py migrate
    ```
6. Ejecuta el servidor de desarrollo:
    ```bash
    python manage.py runserver
    ```

## Uso

Accede a la aplicación en [http://localhost:8000](http://localhost:8000).  
Puedes gestionar horarios, disponibilidad y más desde la interfaz web.

## Estructura del proyecto

- **/templates/**: Archivos HTML.
- **/app/**: Lógica principal en Python (Django).
- **manage.py**: Script de gestión de Django.

## Contribuciones

¡Se aceptan contribuciones! Por favor, abre un issue o pull request para sugerencias o mejoras.

