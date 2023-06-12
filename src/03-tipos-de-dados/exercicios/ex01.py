''' solicite ao usuário 3 números, armazene esses elementos em uma 
lista e apresente no final o menor e maior elemento numeros'''

numeros = []

while len(numeros) < 3:
    numeros.append(float(input("Digite três números: ")))

maior = numeros[0]
menor = numeros[0]
for numero in numeros:
    if numero > maior:
        maior = numero
    elif numero < menor:
        menor = numero

print(f"O maior número é: {maior}")
print(f"O menor número é: {menor}")