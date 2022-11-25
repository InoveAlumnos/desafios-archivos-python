# desafios-archivos-python

Repositorio con archivos que se utilizan en el módulo 7 (archivos) del curso inicial, convertidos a `.json`
para que sea más sencillo realizar tests sobre esos ejercicios.

Cada `json` contienen sólo las primeras 10 filas del archivo al que corresponde.

El archivo `convert.py` puede utilzarse para convertir de `csv` a `json`
```py
python convert.py
Enter the name of the file: <filename> # Nombre del archivo (con la extensión)
```

# Cómo solicitar el contenido de los archivos (desde python)

```python
data = requests.get(f"https://raw.githubusercontent.com/InoveAlumnos/desafios-archivos-python/main/json/{filename}", stream = True)
data = data.json()
```
Donde `filename` puede variar entre:
- propiedades.json
- ironman.json
- stock.json