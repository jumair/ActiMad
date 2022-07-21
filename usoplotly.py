import pandas as pd
import plotly.express as px

# Abro el fichero donde tengo las actividades filtradas y correctas para representarlas de forma muy sencilla en un mapa
ruta = 'D:/GitHub/ActiMad/'
actividades = pd.read_csv(ruta + "actividades-100-fin.csv")

# Preparo el mapa. Al ponerse encima de los puntos rojos aparece información (titulo, distrito, barrio, longitud y latitud) de la actividad.
fig = px.scatter_mapbox(actividades, lat="Latitud", lon="Longitud", hover_name="Titulo", hover_data=["Distrito", "Barrio"],
                        color_discrete_sequence=["red"], zoom=11, height=700)

fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
# Muestra el mapa en un navegador
fig.show()
# Genera un fichero html en la misma carpeta
fig.write_html( ruta + "mapa_acti_mad.html")