#  Desafio com Funções

'''
Criar um programa que calcula a quantidade de tinta necessária para pintar uma parede. 
O usuário deverá forncecer as seguintes informações: Rendimento, altura e largura.

O programa deve mostrar na tela a mensagem 'Você necessita de x latas de tina'


'''

rend_lata = int(input('Qual é o rendimento da lata? '))
alt_parede = int(input('Qual é a altura da parede? '))
larg_parede = int(input('Qual é a largura da parede? '))

def calculo_tinta():
    area = alt_parede * larg_parede
    total = area / rend_lata
    print(f'Você precisa de {total} latas de tinta')

calculo_tinta()