# pythonPrograms
A repository for my learning programs on python

## Indice

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
- Números enteros
```python
    integer_number = 1
```
- Números flotantes
```python
    float_number = 1.5
```
- Cadena de texto
```python
    string = "hola"
```
- Cadena de texto con varias lineas
```python
    multi_line_string = """
    linea 1
    linea 2
    linea 3
    """
```
- Booleanos
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

## Errores
Siempre que codifiquemos tendremos algun error, pues no somos perfectos, por lo que en python hay distintos tipos de errores.

A rasgos muy generales, hay dos grupos de errores, el primero donde **python nos dice que nos equivocamos** y el otro **Donde no nos dice**.

Si corremos con la suerte que python nos diga que nos equivocamos, normalmente veremos algo como esto: 
> File "ruta del archivo", line 16, in "modulo"
>   run()
>  File "ruta del archivo", line 10, in run
>    "Expresion que genera el codigo"
>"Tipo de Error": "Mensaje de error"
