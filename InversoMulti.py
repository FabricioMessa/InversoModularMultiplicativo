a = int(input("Digite el primer numero: "))
n = int(input("Digite el segundo numero: "))

if n < 0:
    n = int(input("El entero debe ser positivo, favor de digitar de nuevo el numero: "))
    print("== Nuevos numeros digitados ==")
    print(a)
    print(n)
else:
    print("== Numeros digitados ==")
    print(a)
    print(n)

def inverso_modular_multiplicativo(a, n):
    for i in range(1, n):
        if (a % n) * (i % n) % n == 1:
            return i
    if (a % n) * (i % n) % n != 1:
        print("No tiene Inverso Modular Multiplicativo")

print("Procedemos a hallar el Inverso Modular Multiplicativo")
inv_mod_mult = inverso_modular_multiplicativo(a, n)
print("El resultado buscado es: " + str(inv_mod_mult))


