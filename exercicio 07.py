""" DESAFIO 07:
- Informe o salario e realize um aumento de 15% e exiba o acrescimo sob o valor atual.
- Retorne o resultado."""

salario = float(input("Digite o salario: "))
aumento = (15/100) * salario
nsalario = salario + aumento
print("O salario com 15% de aumento é R${:.2f} e tem acrescimo de R${:.2f}".format(nsalario, aumento))