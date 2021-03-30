import random
import time

opciones = ['Piedra', 'Papel', 'Tijera']

print('''Elige una opción:
        1-Piedra 
        2-Papel
        3-Tijera''' )

tu = input('Ingresa 1, 2 o 3: ')
try:
    tu = int(tu)-1
except:
    tu = 'error'

if tu == 'error':
    print('Ingresa un caracter válido.')

else:
    if tu == 0 or tu == 1 or tu == 2:
        print('Tu selección fue:', opciones[tu])
        magia = random.randint( 0, 2)
        compu = opciones[magia]
        time.sleep((1))
        print('Computadora pensando.....')
        time.sleep((1))
        print('Elección de la computadora:', compu)
        
        if tu == magia: 
            print('¡Empate!')

        if tu == 0 and compu == 'Papel':
            print('¡Perdiste!')
        if tu == 0 and compu == 'Tijera':
            print('¡Ganaste!')
            
        if tu == 1 and compu == 'Tijera':
            print('¡Perdiste!')
        if tu == 1 and compu == 'Piedra':
            print('¡Ganaste!')
        
        if tu == 2 and compu == 'Papel':
            print('¡Ganaste!')
        if tu == 2 and compu == 'Piedra':
            print('¡Perdiste!')
    else:
        print('Ingresa un número válido.')
