# ProyectoModulo7
Repositorio creado con la finalidad de albergar los datos para una app de visualizacion estadistica en la web.
# Dashboard de Análisis de Vehículos Usados

Este proyecto es una aplicación web interactiva creada con **Streamlit** que permite explorar un conjunto de datos de anuncios de venta de vehículos en EE.UU.

## Descripción
La aplicación visualiza hallazgos clave obtenidos durante el Análisis Exploratorio de Datos (EDA), enfocándose en la relación entre el precio, el kilometraje y el tipo de vehículo.

## Funcionalidades
* **Histogramas**: Visualización de la distribución del kilometraje (odómetro).
* **Gráficos de Dispersión**: Análisis de la relación entre el precio de venta y el desgaste del vehículo.
* **Filtros Interactivos**: Botones y casillas de verificación para explorar categorías específicas de vehículos.

## Tecnologías Utilizadas
* Python 3.9.6
* Pandas
* Plotly Express
* Streamlit

## Cómo ejecutar localmente
1. Clonar el repositorio.
2. Crear un entorno virtual: `python3 -m venv vehicles_env`.
3. Activar el entorno e instalar dependencias: `pip install -r requirements.txt`.
4. Ejecutar la app: `streamlit run app.py`.