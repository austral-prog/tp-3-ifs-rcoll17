def calculator():
    """
    Ejercicio 7 - Calculadora Simple

    Leer dos números (pueden ser decimales) y una operación (+, -, *, /) mediante input().
    Realizar la operación correspondiente e imprimir el resultado.

    Validaciones:
    - Si la operación es inválida, imprimir "Operacion invalida"
    - Si es división y el divisor es cero, imprimir "Error: division por cero"

    Ejemplo:
        Para las entradas "10", "5" y "+", la salida esperada es:
        Resultado: 15.0

        Para las entradas "10", "2" y "/", la salida esperada es:
        Resultado: 5.0

        Para las entradas "10", "0" y "/", la salida esperada es:
        Error: division por cero

        Para las entradas "10", "5" y "x", la salida esperada es:
        Operacion invalida
    """
    a=float(input())
    b=float(input())
    c=input()
    if c=="+":
        suma=(a+b)
        print(f"Resultado: {suma}")
    elif c=="-":
        resta = (a - b)
        print(f"Resultado: {resta}")
    elif c=="*":
        multi=(a*b)
        print(f"Resultado: {multi}")
    elif c == "/" and b == 0:
        print("Error: division por cero")
    elif c=="/":
        div=(a/b)
        print(f"Resultado: {div}")

    else:
        print("Operacion invalida")

