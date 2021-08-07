
## USO DE yield, con for anidado
def devuleveCiudades(*ciudades): # el * es porque recibe un numero indefinido de elementos
    for elemento in ciudades:
        for subElemento in elemento:
            yield subElemento
        

ciudades_devueltas = devuleveCiudades("Chihuahua", "Juárez","Camargo")

print(next(ciudades_devueltas)) # C, subelemento del elemento, caracter de una palabra
print(next(ciudades_devueltas)) # h, subelemento del elemento, caracter de una palabra
print(next(ciudades_devueltas)) # i, subelemento del elemento, caracter de una palabra

## USO DE yield form (para no usar for anidado)
def devuleveCiudades2(*ciudades): # el * es porque recibe un numero indefinido de elementos
    for elemento in ciudades:
        yield  from elemento
        

ciudades_devueltas2 = devuleveCiudades("Chihuahua", "Juárez","Camargo")

print(next(ciudades_devueltas2))# C, subelemento del elemento, caracter de una palabra
print(next(ciudades_devueltas2))
print(next(ciudades_devueltas2))