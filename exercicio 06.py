""" DESAFIO 06:
- Informe a largura e altura (em metros) de uma parede, calcule a área e informe quanto de tinta será necessário para pintar.
- Sabendo que uma lata de tinta consegue pintar 2m²
- Retorne o resultado."""

largura = float(input("Digite a largura em metros: "))

altura = float(input("Digite a altura em metros: "))

area = largura*altura

tinta = area // 2

if area % 2 != 0:
    tinta += 1    

print("Área da parede é de {} m² e será preciso {:0.0f} latas de tinta.".format(area,tinta))