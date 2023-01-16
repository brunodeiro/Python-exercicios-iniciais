""" DESAFIO 01:
- Informe a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
- Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado."""

km = float(input("Informe a quantidade de Km percorridos pelo carro alugado: "))

dias = float(input("Informe a quantidade de dias pelos quais ele foi alugado: "))

preco = (km * 0.15) + (dias * 60)


print("Aluguel do carro custa R$60,00 por dia e R$0,15 por Km rodado.")
print("O preço a pagar é de R${:0.2f}".format(preco))