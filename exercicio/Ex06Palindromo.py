frase = input("Digite uma frase: ")

frase = frase.replace(" ", "").lower()

if frase == frase[::-1]:
    print("É um palíndromo!")
else:
    print("Não é um palíndromo.")