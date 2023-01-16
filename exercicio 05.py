""" DESAFIO 05:
- Informe um valor em metros, converta em centimetros e milimetros .
- Retorne o resultado."""

n1 = int(input("Digite um numero: "))

cent = n1 * 100

mili = cent * 10

print("{} metro(s) equivale a {} centimetro(s) e {} milimetro(s)".format(n1, cent, mili))