""" DESAFIO 08:
- Digite um numero e exiba a tabuada desse numero.
- Retorne o resultado."""

n1 = int(input("Digite um numero: "))

print("\nAdição")
for i in range(1, 10, 1):
    print("{} + {} = {}".format(n1, i, n1 + i))

print("\nSubtração")
for i in range(1, 10, 1):
    print("{} - {} = {}".format(n1, i, n1 - i))

print("\nMultiplicação")
for i in range(1, 10, 1):
    print("{} X {} = {}".format(n1, i, n1 * i))

print("\nDivisão")
for i in range(1, 10, 1):
    print("{} / {} = {:.3f}".format(n1, i, n1 / i))