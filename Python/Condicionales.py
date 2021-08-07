
# CONDICIONAL IF, elif (else if)

numero=10;


if 10>numero:
    print("10 es mayor")
elif 10<numero:
    print("10 No es mayor")
else: #Como se está usando elif, este else es relativo al primer if
    print("son iguales")


numero1=15;
numero2=25;
# and
if numero1>0 and numero2>10:
    print("Ambos numeros son mayores")
    
# or
if numero1>0 or numero2>10:
    print("Ambos numeros son mayores")    
    
# in
nombre = "Carlos1"
if nombre in ("Carlos","Erika"):
    print("Sí se encuentra")
else:
    print("No se encuentra")