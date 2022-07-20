# ActiMad - 20/07/2022
Lee las actvidades culturales de Madrid desde API en formato csv 

### Desarrollado en Python
Usa una API del ayuntamiento de Madrid para leer las actividades culturales.
Hace uso de las librerias request, pandas y plotly.express de python.

Es una aplicación sencilla que lee este fichero en formato csv y después de hacer un tratamiento sencillo del fichero con pandas lo muestra en un mapa.

### Instalación

Deberías tener instalado python 3.10 - Para instalar python ir a https://www.python.org/downloads/
Se pueden ejecutar los ficheros desde Visual Studio Code ue es gratis y se puede descargar desde https://code.visualstudio.com/download

### Ficheros

Puedes descargar los ficheros y guardarlos en la siguiente ruta 'D:/PythonDimas/JSON/'
Si quieres cambiar la ruta sólo tienes que cambiar la variable **ruta** que está al principio de los 2 ficheros de python.

**leercsvmadridapi.ipynb**  
Es un Jupyter Notebook que se puede ejecutar desde Visual Studio Code. Lo he hecho en este formato para poder ejecutarlo por partes e ir viendo los resultados poco a poco. 

Este fichero lee el fichero **https://datos.madrid.es/egob/catalogo/206974-0-agenda-eventos-culturales-100.csv** desde la API, guarda el fichero **actividades-100.csv** para trabajar con el y hacer algunas operaciones con la librería pandas para crear el fichero **actividades-100-fin.csv**

**usoplotly.py**  
es un fichero de python normal.  

Este fichero lee el fichero **actividades-100-fin.csv** ya filtrado anteriormente y muestra en un mapa sencillo las actividades culturales.  
  
***
    
#### * *También hay una copia de los archivos de datos **actividades-100.csv** y **actividades-100-fin.csv**.*
