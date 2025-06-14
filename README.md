# Informe de Asistencias y Ausencias - Proyecto Python

Este proyecto permite cargar, filtrar y analizar archivos Excel con información de asistencias y ausencias de estudiantes por grado y día. Además, genera gráficos que resumen estas estadísticas y envía un informe por correo electrónico con los gráficos embebidos.

---

## Características Principales

- **Carga y filtrado automático** de múltiples archivos Excel dentro de una carpeta.
- **Conteo detallado** de asistencias y ausencias por día y por grado académico.
- **Generación de gráficos** claros y visuales:
  - Gráfico circular con la proporción y cantidad de asistencias y ausencias del último día.
  - Gráfico de barras con el total de ausencias por grado durante el mes.
- **Envio automático de correo electrónico** con los gráficos embebidos para facilitar la visualización y el envío de informes.

---

## Requisitos

- Python 3.7 o superior
- Bibliotecas Python:
  - pandas
  - matplotlib
  - openpyxl (para leer archivos Excel)
- Acceso a un servidor SMTP (por defecto usa Outlook con `smtp.office365.com`).

Puedes instalar las dependencias con:

pip install pandas matplotlib openpyxl

## Configuración

El archivo config.ini es necesario para configurar los datos del correo electrónico. Debes crear un archivo con la siguiente estructura y completar con tus datos personales:

[EMAIL]
SMTP_SERVER = smtp.office365.com
SMTP_PORT = 587
EMAIL_SENDER = tu_correo@ejemplo.com
EMAIL_PASSWORD = tu_contraseña
EMAIL_RECEIVER = correo_destinatario@ejemplo.com

## Uso
Coloca tus archivos Excel (.xlsx) con datos de asistencias en la carpeta files/.
Ejecuta el script principal:


python main.py
El programa:
Carga y filtra los datos excluyendo filas que contienen textos no deseados.
Calcula asistencias y ausencias.
Genera gráficos informativos.
Envía un correo electrónico con los gráficos adjuntos.
Estructura del Proyecto
main.py : Script principal que orquesta la ejecución.
config.ini : Archivo de configuración para el correo electrónico.
data_loading.py : Funciones para cargar y filtrar datos Excel.
data_processing.py : Funciones para conteos y agregaciones.
data_visualization.py : Funciones para creación de gráficos.
email_utils.py : Funciones para el envío de correos electrónicos.
Notas importantes
Asegúrate de que la carpeta files exista y contenga los archivos Excel.
El correo configurado debe permitir acceso SMTP con el usuario y contraseña proporcionados.
El script no procesa datos si los archivos están vacíos o todos los datos son filtrados.
Contacto
Si tienes dudas o quieres contribuir, contacta a [tu correo o github].

Este proyecto utiliza buenas prácticas de modularización y es fácilmente ampliable o adaptable según necesidades futuras.