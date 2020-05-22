# Control de Ingreso
TIA SA
## Instalacion

1. Montar el ambiente virtual.
2. Instalar las dependencias.
3. Configurar la base de datos en el settings.py
4. Realizar las migraciones 
```python
py manage.py makemigrations
```
5. Migrar a la base de datos 
```python
py manage.py migrate
```
6. Crear el super usuario admin 
```python
py manage.py createsuperuser
```
7. Correr el servidor 
```python
py manage.py runserver
```
 o deploy en el server.