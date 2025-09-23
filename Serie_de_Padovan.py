def padovan(numero):
    padovan = [1, 1, 1]
    for i in range(3, numero+1):
        siguiente = padovan[i-2] + padovan[i-3]
        padovan.append(siguiente)
    return padovan[numero]
print(padovan(7))
print(padovan(10))
print(padovan(100))