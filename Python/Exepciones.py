
def pruebaException():
    
    try:
        total = 10/0
    
        return total

    except:
        print("Hubo un problema")
    
pruebaException()