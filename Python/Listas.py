
# CREAR LISTA
miLista=["Carlos","Erika","Dana","Brenda","Lana"]

# OBTENER VALORES
print(miLista[:]) # ["Carlos","Erika","Dana","Brenda","Lana"]
print(miLista[2]) # Dana
print(miLista[2:5]) # ["Dana","Brenda","Lana"]    
print(miLista[-2]) # Brendas

# AGREGAR ELEMENTO A LA LISTA
miLista.append("Tales")
print(miLista)

# AGREGAR ELEMENTOS A LA LISTA
miLista.extend(["Goyo", "Eiden"])
print(miLista)

# OBTENER INDICE DE ELEMENTOS (regrese el primero que encuentre)
print(miLista.index("Eiden"))

# SABER SI UN ELEMENTO EXISTE
print("Eiden" in miLista)
print("Eiden222" in miLista)

# ELIMINAR UN ELEMENTO
print(miLista.remove("Eiden"))
print(miLista)

# ELIMINAR ÚLTIMO  ELEMENTO
miLista.pop()
print(miLista)

# CREAR LISTA ELEMENTOS DIFERENTE
miLista2=["Carlos",11, True,77.99]
print(miLista2) # ["Carlos",11, True,77.99]

# SUMAR LISTAS
miLista3 = miLista +miLista2
print(miLista3)  # ['Carlos', 'Erika', 'Dana', 'Brenda', 'Lana', 'Tales', 'Carlos', 11, True, 77.99]

