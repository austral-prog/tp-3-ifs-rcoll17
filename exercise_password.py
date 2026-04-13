def password():
    """
    Ejercicio 10 - Validador de Contraseña

    Leer una contraseña mediante input(). Validar que cumpla con los siguientes requisitos:
    1. Debe tener al menos 8 caracteres de longitud
    2. Debe contener al menos un número (usar el operador in para verificar cada dígito del 0 al 9)

    Si cumple ambos requisitos, imprimir "Contraseña valida".
    Si no cumple, imprimir cuál requisito falta.

    Ejemplo:
        Para la entrada "abc12345", la salida esperada es:
        Contraseña valida

        Para la entrada "abc123", la salida esperada es:
        Contraseña muy corta

        Para la entrada "abcdefgh", la salida esperada es:
        Debe contener un numero

        Para la entrada "abc", la salida esperada es:
        Contraseña muy corta
        Debe contener un numero
    """
    a=input()
    b=len(a)
    c="1" in a or "2" in a or "3" in a or "4" in a or "5" in a or "6" in a or "7" in a or "8" in a or "9" in a

    if b>=8 and c:
        print("Contraseña valida")
    elif b<8 and c:
        print("Contraseña muy corta")
    elif b>=8 and not c:
        print("Debe contener un numero")
    else:
        print("Contraseña muy corta")
        print("Debe contener un numero")

