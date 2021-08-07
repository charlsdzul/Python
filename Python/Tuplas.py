
#CREAR TUPLA
miTupla = ("Carlos", 11, 123.25, True,"Carlos")
miTuplaAlterna = "Carlos", 11, 123.25, True,"Carlos" # empaquetado de tupla
print(miTupla)
print(miTuplaAlterna)

# Sí acepta búsqueda por index

#CREAR LISTA A PARTIR DE UNA TUPLA
miLista = list(miTupla)
print(miLista)

#CREAR tupla A PARTIR DE UNA lista
miTupla2 = tuple(miLista)
print(miTupla2)

# SABER SI EXISTE UN ELEMENTO EN UNA tupla
print("Carlos" in miTupla2)

# CUÁNTOS ELEMENTOS SE ENCUENTRAN EN LA tupla
print(miTupla2.count("Carlos"))

# LONGITUD DE UNA tupla
print(len(miTupla2))

# DESEMPAQUETADO DE TUPLAS
miTupla3 = ("Carlos", 11, 123.25, True,"Carlos")
nombre, dia, cantidad, esPersona, apellido = miTupla3
print(cantidad)