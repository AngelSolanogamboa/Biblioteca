# Usar la imagen oficial de Python
FROM python:3.12-slim-bullseye

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /config

# Copiar el archivo de requerimientos y luego instalarlos
COPY requirements.txt /config/
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del proyecto a la carpeta de trabajo
COPY . /config/

# Exponer el puerto 8000 para el servidor Django
EXPOSE 8000

# Comando para ejecutar la aplicación Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]