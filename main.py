def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError("no puede dividir por cero")
    return a / b

def guardar_log(operacion, resultado):
    with open("logs/log.txt", "a") as archivo:
        archivo.write(f"{operacion} = {resultado}\n")

if __name__ == "__main__":
    print("Calculadora interactiva")
    print("1. Sumar\n2. Restar\n3. Multiplicar\n4. Dividir")
    opcion = input("Elige una opción: ")

    a = float(input("Primer número: "))
    b = float(input("Segundo número: "))

    try:
        if opcion == "1":
            resultado = sumar(a, b)
            guardar_log(f"{a} + {b}", resultado)
        elif opcion == "2":
            resultado = restar(a, b)
            guardar_log(f"{a} - {b}", resultado)
        elif opcion == "3":
            resultado = multiplicar(a, b)
            guardar_log(f"{a} * {b}", resultado)
        elif opcion == "4":
            resultado = dividir(a, b)
            guardar_log(f"{a} / {b}", resultado)
        else:
            resultado = "Opción inválida"
            print(resultado)
            exit()

        print(f"Resultado: {resultado}")
    except ZeroDivisionError as e:
        print(f"Error: {e}")

