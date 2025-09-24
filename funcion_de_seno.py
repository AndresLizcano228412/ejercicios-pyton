x = 1.5707963267948966
n = 12
seno = 0
for i in range(n+1):
    signo = (-1) ** i
    exponente = 2 * i + 1
    potencia = x ** exponente
    factorial = 1
    for k in range(1, exponente + 1):
        factorial *= k
    termino = signo * (potencia / factorial)
    seno += termino
    print(f"termino {i}: {termino}")
print(f"Seno({x}) = {seno}")