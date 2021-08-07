
###CICLO FOR
for i in range(5): #cuenta desde 0 hasta 4
    print("HOLA #: ", i)

for i in range(5,10): #cuenta desde 5 hasta 9
    print("HOLA: "+ str(i), end="_")    

for i in range(5,50,3): #cuenta desde 5 hasta 49, sumando 3
    print("HOLA "+ str(i), end="_")      

# se recorre 3 veces, porque hay 5 elementos en la tupla
for i in ["1","2","3","","5"]:
    print("Hola: "+i)

# 'end' agrega string al final del print
for i in ["1","2","3","","5"]:
    print("HOLA: "+i, end="__")
    
#  el for hace el recorrido el numero de veces de los caracteres del string
arroba = False
punto = False

for i in "carlos@hotmail.com":
    if(i=="@"):
        arroba=True
    
    if(i=="."):
        punto=True

if arroba and punto:
    print("Email es correcto")
else:
    print("Email no es correco")