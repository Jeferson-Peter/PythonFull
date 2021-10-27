# + - * / ** %  // math.sqrt

# operator = 25 **(1/2) #raiz quadrada sem math.sqtr
import math
# operator = math.sqrt(25)

operator =  5+ 5 - 2 * 3

#raiz quadrada e exponeciação seram os primeiros a executar
# multiplização e divisão são os segundoa
# e só por final soma e subtração
# () possuem precedência principal

a = input('Informe o valor de a: ')
b = input('Informe o valor de b: ')

soma = a + b
print(f'A soma de {a} + {b} = {soma}')
subtract = a - b
print(f'A subtração de {a} - {b} = {subtract}')
multiply = a *  b
print(f'A multiplicação de {a} * {b} = {multiply}')
divide = a / b
print(f'A divide da {a} / {b} = {divide}')
exponent =  a ** b
print(f'A exponent da {a} ** {b} = {exponent}')
