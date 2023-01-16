""" DESAFIO 02: 
Dois valores inteiros serão inseridos e deve obter como retorno:
    - A soma dos valores.
    - A subtração dos valores.
    - A multiplicação dos valores.
    - A divisão dos valores.
    - A divisão inteira dos valores.
    - A potenciação dos valores. (faça com dois métodos diferentes)
    - O resto da divisão dos valores.     
"""

n1 = int(input("Digite um valor: "))

n2 = int(input("Digite outro valor: "))


soma = n1 + n2
sub = n1 - n2
mult = n1 * n2
div = n1 / n2
divint = n1 // n2
pot = n1 ** n2
pot2 = pow(n1,n2)
resto = n1 % n2

print("O resultado da soma dos valores {} e {} é {}".format(n1, n2, soma))
print("O resultado da subtração é {}".format(sub))
print("O resultado da multiplicação é {}".format(mult))
print("O resultado da divisão é {}".format(div))
print("O resultado da divisão inteira é {}".format(divint))
print("O resultado da potenciação é {}".format(pot))
print("O resultado da potenciação (método alternativo) é {}".format(pot2))
print("O resultado do resto da divisão é {}".format(resto))

# Retornar também a raiz quadrada da soma dos valores.

print("O resultado da raiz quadrada é: {:.2f}".format(soma**(1/2)))