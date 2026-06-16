print("Calculadora")

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
soma = num1 + num2
print("A soma dos números é:", soma)
subtracao = num1 - num2
print("A subtração dos números é:", subtracao)
multiplicacao = num1 * num2
print("A multiplicação dos números é:", multiplicacao)
if num2 != 0:
    divisao = num1 / num2
    print("A divisão dos números é:", divisao)
else:    print("Não é possível dividir por zero.")