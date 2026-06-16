print("Conta Vogais")

def contar_vogais(frase):
    vogais = "aeiouAEIOU"
    contador = 0
    for letra in frase:
        if letra in vogais:
            contador += 1
    return contador
frase_usuario = input("Digite uma frase: ")
total_vogais = contar_vogais(frase_usuario)
print(f"A frase '{frase_usuario}' contém {total_vogais} vogais.")