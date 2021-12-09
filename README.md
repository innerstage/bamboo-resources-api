# Bamboo Resources API
A Flask API designed to return sample data for Bamboo resources.


# Instrucciones para Domi 👩🏻‍💻

## Flask 🌶
Flask es un framework de backend que permite desarrollar aplicaciones web completas con Python, la aplicación es un script sencillo que se encuentra en `application.py` y necesitas instalar Flask en un entorno virtual de Python para utilizarlo:

* Verifica que tienes instalado Python 🐍, ojalá Python 3.10 o 3.9, puedes chequear tu versión global con `python3 -V` en la terminal.
* Crea un entorno virtual dentro de este repositorio: `python3 -m venv venv`.
* Actívalo con `source venv/bin/activate`.
* Instala Flask con `pip install Flask`.
* Ejecuta la aplicación con `flask run`.

**Referencia**: https://flask.palletsprojects.com/en/2.0.x/installation/


## Creación de archivos estáticos
En este mismo repositorio, crea los archivos estáticos con datos falsos o algo que sientas que apoye los ejemplos de la mejor manera posible, bien pedagógico, con la complejidad justa. Te recomiendo investigar una librería de Python que se llama `Faker` para crear datos falsos en DataFrames y luego puedes usar `df.to_csv("nombre_de_archivo.csv", index=False, quoting=csv.QUOTE_NONNUMERIC)` para que guarde los datos en un archivo (importa `csv` en tu script para tener el quoting, es el mecanismo para ponerle comillas a los valores). Da lo mismo cómo inventes los datos, puede ser en un notebook o con un script, lo que importa es el resultado final.

# Servir los archivos estáticos con Flask
Encontré esto para servir los archivos estáticos:

```
from flask import Flask, request, send_from_directory

# set the project root directory as the static folder, you can set others.
app = Flask(__name__, static_url_path='')

@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('js', path)

if __name__ == "__main__":
    app.run()
```

Se supone que así se define una ruta y el archivo tiene que estar dentro de una carpeta que se llama `static` para que funcione.

# Crear APIs
Usaremos APIs para ejemplos más complejos de `DownloadStep` o parametrización, lo que desarrolles debería dar respuestas en JSON u otros formatos según corresponda, esto lo podemos ir haciendo juntos, y conversar sobre los requerimientos, de todo en realidad... trataré de darte especificaciones bien acotadas.

# Cosas por hacer:
- [ ] #1. Crear un archivo CSV con varias columnas y filas: Basado en mi repositorio de datos ficticios (tienda de verduras) https://github.com/innerstage/fictitious-dataset.git.
- [ ] #2. Subirlo a una instancia de AWS S3, hablar con @Dave a ver si tenemos una cuenta de AWS de Datawheel.
- [ ] #3. Subirlo a un GCP Storage Bucket, en el proyecto Bamboo.
- [ ] #4. Crear una versión comprimida del archivo (`.zip`) y servirlo mediante Flask también.
- [ ] #5. Crear dos o tres archivos de datos ficticios, que funcionen en conjunto para armar toda la información (pregúntame de esto jajaja), y que ambos sean servidos por Flask.
- [ ] #6. Subir los archivos anteriores también al Bucket de GCP.
- [ ] #7. Diseñar un API en Flask que entregue respuestas en JSON:
    * Instala `sqlite3` en tu compu para trabajar con esta base de datos pequeña, crea el archivo `database.db` en este repositorio y crea una tabla que almacene varios datos de venta (años 2010 - 2020), por ejemplo, `fictitious-dataset` hace eso fácilmente, lo más complicado es cómo insertar los datos en la base de datos, pero con un script de Python se puede fácil.
    * El endpoint debería funcionar como `/api/<year>`, según el año que se pase, debería agregar las ventas totales de cada mes y retornarlo como JSON, onda:
    ```
    [
        {
            "year": 2010,
            "month": 1,
            "month_name": "January",
            "total_sales": 283564.89
        },
        {
            "year": 2010,
            "month": 2,
            "month_name": "February",
            "total_sales": 637163.32
        },
        ...
    ]
    
    ```