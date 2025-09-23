def isDigitIncreasing(numero):
    for a in range(1, 10):  
      suma=0
      valor=0
      for b in range(len(str(numero))):
         valor = valor * 10 + a
         suma += valor
         if suma == numero:
            return 1
         if suma > numero:
                  break
    return 0  
print(isDigitIncreasing(30))
