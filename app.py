#https://app-dashboard-c8d89obi4delcqph6eylbq.streamlit.app/

###############################################################3
# Resumen del Dashboard
#######################
# Entrada del usuario (nombre, año, mes, color del gráfico).
# Gráfico de líneas mostrando las ventas mensuales.
# Gráfico de barras con el rendimiento de empleados.
# Mapa interactivo con la distribución geográfica de clientes.
# Filtros dinámicos en la barra lateral.
# Mensaje de bienvenida personalizado.
################################################################

# Se importan las liberias necesarias para el Dashboard
# streamlit → Librería principal para crear la interfaz del dashboard.
# pandas → Manejo de datos en formato tabular (DataFrames).
# numpy → Generación de datos numéricos aleatorios.
# matplotlib.pyplot → Creación de gráficos (líneas y barras).
# folium → Creación de mapas interactivos.
# streamlit_folium → Integración de mapas de folium dentro de Streamlit.
#
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import folium
from streamlit_folium import folium_static

#
# Título y descripción del dashboard
#
# st.title() → Título principal del dashboard.
# st.markdown() → Subtítulo o descripción del panel de análisis.
#
# Configuración del título del Dashboard
st.title("Dashboard Interactivo de DataTech Solutions")
st.markdown("## Análisis de ventas, rendimiento de empleados y clientes")

# Sidebar - Configuración de filtros
#
# st.sidebar.header() → Título de la barra lateral.
# st.sidebar.text_input() → Entrada de texto para el usuario.
# st.sidebar.selectbox() → Desplegables para seleccionar año y mes.
# st.sidebar.color_picker() → Selector de color para personalizar los gráficos.
#
st.sidebar.header("Configuración")
nombre_usuario = st.sidebar.text_input("Ingresa tu nombre", "Usuario")
year = st.sidebar.selectbox("Selecciona el año", [2021, 2022, 2023])
mes = st.sidebar.selectbox("Selecciona el mes", list(range(1, 13)))
color_grafico = st.sidebar.color_picker("Selecciona el color del gráfico", "#3498db")

# Generación de datos ficticios
# Garantiza que los datos aleatorios sean reproducibles.
np.random.seed(42)

# Ventas mensuales por producto
# Se genera una tabla con ventas mensuales ficticias
meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
ventas = np.random.randint(1000, 5000, size=12)
df_ventas = pd.DataFrame({"Mes": meses, "Ventas": ventas})

# Gráfico de Ventas Mensuales
#
# Se crea un gráfico de líneas con matplotlib.
# Se usa el color elegido por el usuario en color_grafico.
# Se muestra con st.pyplot(fig).
# Resultado: Un gráfico de líneas mostrando la evolución de las ventas.
#
st.subheader("Ventas Mensuales")
fig, ax = plt.subplots()
ax.plot(df_ventas["Mes"], df_ventas["Ventas"], marker="o", color=color_grafico)
ax.set_xlabel("Mes")
ax.set_ylabel("Ventas")
ax.set_title("Tendencia de Ventas Mensuales")
plt.xticks(rotation=45)
st.pyplot(fig)

# Rendimiento de empleados por departamento
# Se genera una tabla con rendimiento ficticio por departamento
departamentos = ["Ventas", "Soporte", "Desarrollo", "Marketing"]
rendimiento = np.random.randint(50, 100, size=len(departamentos))
df_rendimiento = pd.DataFrame({"Departamento": departamentos, "Rendimiento": rendimiento})

# Gráfico de Barras de Rendimiento de Empleados
#
# Se genera un gráfico de barras con matplotlib.
# Se usa el color elegido por el usuario en color_grafico.
# Se muestra con st.pyplot(fig).
# Resultado: Un gráfico de barras mostrando el rendimiento de cada departamento.
#
st.subheader("Rendimiento de Empleados")
fig, ax = plt.subplots()
ax.bar(df_rendimiento["Departamento"], df_rendimiento["Rendimiento"], color=color_grafico)
ax.set_xlabel("Departamento")
ax.set_ylabel("Rendimiento (%)")
ax.set_title("Rendimiento por Departamento")
st.pyplot(fig)

# Distribución geográfica de clientes
# Se generan 10 ubicaciones aleatorias de clientes.
latitudes = np.random.uniform(-10, 50, 10)
longitudes = np.random.uniform(-80, 20, 10)
df_clientes = pd.DataFrame({"Latitud": latitudes, "Longitud": longitudes})

# Mapa de Clientes
#
# Se genera un mapa interactivo con folium.
# Se colocan marcadores en el mapa para representar clientes.
# Se usa folium_static(m) para visualizarlo en Streamlit.
# Resultado: Un mapa interactivo con la distribución de clientes.
#
st.subheader("🌍 Distribución Geográfica de Clientes")
m = folium.Map(location=[20, -40], zoom_start=2)
for _, row in df_clientes.iterrows():
    folium.Marker([row["Latitud"], row["Longitud"]], popup="Cliente").add_to(m)
folium_static(m)

# Mensaje de despedida
#
# Se muestra el nombre del usuario en la barra lateral.
# Se muestra un mensaje de bienvenida en la pantalla principal.
#
st.sidebar.markdown(f"👤 Usuario activo: **{nombre_usuario}**")
st.success(f"¡Bienvenido, {nombre_usuario}! Esperamos que disfrutes del análisis.")

