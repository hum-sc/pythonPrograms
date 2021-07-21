# pythonPrograms
A repository for my learning programs on python

## Operaciones
En python hay (como en todo lenguaje de programacion) una forma especifica de escribir operaciones matematicas, las cuales serán listadas a continuacion.

### Suma
```python
    1+3
```
### Resta
```python
    1-3
```
### Multiplicacion
```python
    1*3
```
### Division
```python
    1/3
```
### Division entera
```python
    1//3
```
### Residuo
```python
    1%3
```
### Potencia
```python
    1**3
```

## Variables
En python las variables son objetos que almacenan un valor, pueden ser de cualquier tipo de dato.

Es una caja, en ella puedes meter objetos

### Normas para nombrar variables
- Deben empezar con letras MINÚSCULA
- No deben contener espacios
- No se puede contener espacios
- No puede usar números al inicio


## Objetos
En python todo es un objeto
### Tipos de objetos
- ##### Números enteros
```python
    integer_number = 1
```
- ##### Números flotantes
```python
    float_number = 1.5
```
- ##### Cadena de texto
```python
    string = "hola"
```
- ##### Cadena de texto con varias lineas
```python
    multi_line_string = """
    linea 1
    linea 2
    linea 3
    """
```
- ##### Booleanos
```python
    #Estos solo pueden ser True o False
    boolean = True
```
### Convertir objetos
- A número entero
```python
    float_number = 1.5
    float_number_as_integer = int(float_number)
```
- A número flotante
```python
    integer_number = 1
    integer_number_as_float = float(integer_number)
```
- A cadena de texto
```python
    integer_number = 1
    integer_number_as_string = str(integer_number)
```
- A boolean
```python
    integer_number = 1
    integer_number_as_boolean = bool(integer_number)
```


## Operadores logicos y de comparación
- [ ] ASAP

## Errores
Siempre que codifiquemos tendremos algun error, pues no somos perfectos, por lo que en python hay distintos tipos de errores.

A rasgos muy generales, hay dos grupos de errores, el primero donde **python nos dice que nos equivocamos** y el otro **sonde no nos dice**.

### Python no nos dice
Comunmente, cuando python **no nos dice** es porque el error lo tenemos dentro de la logica de nuestro algoritmo, o por ejemplo, si pedimos ingresar un correo electronico y el usuario ingresa un nombre, python no sabra que hay un error ahi.

Para solucionar esto, podemos verificar nosotros si es un correo, en su defecto podemos lanzar errores usando ***raise***
```python
    raise TypeError("No es un correo electronico")
```
***raise*** lo que hace es crear un objeto de error, y luego lanzarlo a la funcion superior.

### Python nos dice
Si corremos con la suerte que python nos dice que nos equivocamos, normalmente veremos algo como esto: 

> File "ruta del archivo", line 16, in "modulo"

>   run()

>  File "ruta del archivo", line 10, in run

>    "Expresion que genera el error"

>"Tipo de Error": "Mensaje de error"

### Obtener errores y usarlos para ejecutar codigo
Podemos obtener errores usando ***except*** despues de ***try***.
Es decir, Intentamos hacer algo, y si hay una exepcion, hacemos lo otro, como si de un ***if...else*** se tratara pero para el manejo de errores.
```python
    try:
        # codigo a ejecutar
    except TypoDeError:
        # codigo a ejecutar si hay un error
```

## Assert Statements
Son maneras de manejar errores, en esta hay una condicion que debe cumplirse, de lo contrario lanzara un mensaje de error.
```python
    assert condicion, "Mensaje de error"
```
>Afirmo que esta condicion es verdadera, de lo contrario devuelve un mensaje de error.

Devuelve un error de tipo AssertionError.


# Pensamiento Computacional con Python
## Enumeracion Exhaustiva
Se trata de enumerar todas las posibilidades, aunque es muy ineficiente, en la actualidad no importa demasiado pues las computadoras son muy rápidas (obvio hay casos que no son asi).

## Aproximacion de soluciones
Se trata de encontrar una aproximacion de la solucion a un problema, es decir, encontrar una solucion que se aproxime a la solucion exacta.

## Busqueda binaria
Se trata de buscar en la mitad de los datos, y dependiendo si ese dato es mayor o menor discriminas alguna de las dos mitades.
Por ejemplo, si buscas en 