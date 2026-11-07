# biblioteca para aleatoridade

import random

# numero = random(1,10)
# print(numero)

('JOGO DA ALEATORIEDADE...')
print('GANHE ATÉ R$ 5K ')
print('Escolha um número de 1 a 20 ')

numero_maquina = random.randint(1,20)

numero_usuario = int(input(' Escolha o seu número>> '))

numero_maquina = random.randint(1,20)
chances  = 3

for x in range(3):
   print('Voce tem ', chances, 'chances')
   numero_usuario = int(input(' Escolha o seu numero>>'))
   chances  = chances - 1
   if numero_maquina == numero_usuario:
      print('vc ganhou 5k!!')
else:
      print('VC ERROU FEIO!!!')
      if chances == 0:
         print('A MAQUINA ESCOLHEU', numero_maquina)
