""" DESAFIO 04:
- Informe um valor em reais e converta para dolar (cotação atual = 5,12).
- Retorne o resultado."""

n1 = float(input("Digite um valor em reais: "))

dolar = n1 / 5.12

print("Você possui {:.4} dolares".format(dolar))