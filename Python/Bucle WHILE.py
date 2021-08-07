
import math

###CICLO WHILE

i = 1 

while i<=10:
    print("Ejecucion: " + str(i))
    i = i+1
    
    
print("Programa de cálculo de raíz cuadrada")
numero = int(input("Introduce Número:"))

intentos = 0

while numero<0:
    print("No se puede hallar la raiz de un número negativo")
    
    if(intentos==2):
        print("Demasiados intentos")
        break;
    
    numero = int(input("Introduce Número:"))    
    if  numero<0:
        intentos=intentos+10

if intentos<2:
    solucion = math.sqrt(numero)
    print("La raiz cuadrada de " + str(numero) + " es " + str(solucion))