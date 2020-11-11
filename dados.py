import json #modulo que gerencia o json
import moldura, imprime
from math import *

#percorre o dicionario imprimindo somente os dados do produto indicado
def reciclaveis(data, produto):
    for p in data['reciclaveis']:
        if p['material'] == produto:
            moldura.superior()
            imprime.texto(p['material'].upper())
            imprime.texto('Tempo de Degradação: ' + p['tempo_degradacao'])
            imprime.texto('')
            imprime.texto(p['resumo'])
            imprime.texto('')
            imprime.texto('PODEMOS RECICLAR:')
            for i in p['reciclaveis']:
               imprime.texto('✔  ' + i)
            imprime.texto('')
            imprime.texto('NÃO PODEMOS RECICLAR:')
            for i in p['nao_reciclaveis']:
                imprime.texto('✘  ' + i)
            moldura.inferiorDuplo()

def pontosraio(coletas):
    moldura.superior()
    imprime.frase('PONTOS DE COLETA EM UM RAIO')
    imprime.frase('')
    imprime.frase('Se quiser saber como encontrar coordenadas acesse: "support.google.com/maps/answer/18539"')
    imprime.frase('Exemplo: ("-22.926488,-47.037734")')
    moldura.inferior()
    coord = input('Digite a sua latitude e longitude como no formato acima: ')
    coord = coord.split(',')
    raio = float(input('Agora digite o raio (em km) que deseja: '))

    escolhidos = imprime.escolhematerial()

    moldura.superior()
    imprime.frase('PONTOS DE COLETA')
    moldura.inferiorDuplo()
    flag = False
    for p in coletas['pontos']:
        distancia = (6371 * acos(cos(radians(float(coord[0]))) * cos(radians(float(p['coordenadas'][0]))) * cos(radians(float(coord[1])) - radians(float(p['coordenadas'][1]))) + sin(radians(float(coord[0]))) * sin(radians(float(p['coordenadas'][0])))))
        for i in escolhidos:
            if (float(distancia) <= raio) and (i in p['aceita'] or i == 'tudo'):
                flag = True
        if flag: 
            imprime.frase('')
            imprime.frase('')
            imprime.frase(p['nome'])
            for k in p['aceita']:
                imprime.frase(' • ' + k)
            imprime.frase('')
            imprime.frase(' Latitude: ' + str(p['coordenadas'][0]))
            imprime.frase(' Longitude: ' + str(p['coordenadas'][1]))
            imprime.frase(' Distância: ' + str(round(distancia,2)) + ' km')
        flag = False