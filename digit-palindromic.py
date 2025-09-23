def isDigitPalindromic(numero):
    numero_str = str(numero)
    if numero_str == numero_str[::-1]:
        return f"{numero} es digit palindromic."
    else:
        return f"{numero} no es digit palindromic."
    
print(isDigitPalindromic(1331))

