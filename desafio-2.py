'''
2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

IMPORTANTE: Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;'''

times = int(input("Digite o limite até o qual você gostaria de gerar a sequência de Fibonacci: ")) #limite para o cálculo de fibonacci

number = int(input("Digite um número para verificar se pertence à sequência de Fibonacci: "))

#Inicializar
a,b = 0,1

#Armazenar a sequencia
sequencia = [a,b]

while b < times:
      a,b = b, a+b
      sequencia.append(b)
    
print(f"Sequência de Fibonacci gerada até {times}:")
print(sequencia)

if number in sequencia:
      print(f"O número {number} pertence à sequência de Fibonacci.")
else:
      print(f"O número {number} NÃO pertence à sequência de Fibonacci.")
