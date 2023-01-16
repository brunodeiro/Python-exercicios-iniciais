""" DESAFIO 03:
- Informe o preço de um produto, gere um desconto de 5% e aplique sobre o produto.
- Retorne o resultado."""

preco = float(input("Digite o preço do produto: "))

desconto = (5/100) * preco

npreco = preco - desconto

print("O preço com 5% de desconto é R${:.2f} e tem desconto de R${:.2f}".format(npreco, desconto))