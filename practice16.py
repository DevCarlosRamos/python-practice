# practice 16  Crear una Función para Evaluar un Número y Realizar una Operación

# fn(n) si n<=10  10-n : (n*2)+35

def operacion(n):
    """
    we are going to calculate operations with a constraint
    """
    if n<=10:
        return 10-n
    else:
        return (n*2)+35

print(operacion(5))
print(operacion(15))