print("Verificação de Número Par ou Ímpar")
num = int(input("Digite um número inteiro: "))
def verificar_par_impar(numero):
    if numero % 2 == 0:
        return "par"
    else:
        return "ímpar"

resultado = verificar_par_impar(num)
print(f"O número {num} é {resultado}.")