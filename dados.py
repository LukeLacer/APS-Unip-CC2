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

def maisproximo(coletas):
    moldura.superior()
    imprime.frase('PONTO DE COLETA MAIS PRÓXIMO')
    imprime.frase('')
    imprime.frase('Se quiser saber como encontrar coordenadas acesse: "support.google.com/maps/answer/18539"')
    imprime.frase('Exemplo: ("-22.926488,-47.037734")')
    moldura.inferior()
    coord = input('Digite a sua latitude e longitude como no formato acima: ')
    coord = coord.split(',')

    escolhidos = imprime.escolhematerial()

    moldura.superior()
    imprime.frase('PONTO DE COLETA')
    moldura.inferiorDuplo()
    flag = False
    menordistancia = -1

    #procura pelo ponto com menor distancia e grava as coordenadas dele para imprimir depois
    for p in coletas['pontos']:
        distancia = (6371 * acos(cos(radians(float(coord[0]))) * cos(radians(float(p['coordenadas'][0]))) * cos(radians(float(coord[1])) - radians(float(p['coordenadas'][1]))) + sin(radians(float(coord[0]))) * sin(radians(float(p['coordenadas'][0])))))
        if distancia < menordistancia or menordistancia == -1:
            for k in escolhidos:
                if (k in p['aceita'] or k == 'tudo'):
                    menordistancia = distancia
                    menorcoord = p['coordenadas'][:]

    #encontra o ponto que achamos e imprime ele
    for m in coletas['pontos']:
        if float(m['coordenadas'][0]) == float(menorcoord[0]) and float(m['coordenadas'][1]) == float(menorcoord[1]):
            imprime.frase('')
            imprime.frase('')
            imprime.frase(m['nome'])
            for k in m['aceita']:
                imprime.frase(' • ' + k)
            imprime.frase('')
            imprime.frase(' Latitude: ' + str(m['coordenadas'][0]))
            imprime.frase(' Longitude: ' + str(m['coordenadas'][1]))
            imprime.frase(' Distância: ' + str(round(menordistancia,2)) + ' km')

def vertodos(coletas):


    escolhidos = imprime.escolhematerial()

    moldura.superior()
    imprime.frase('PONTO DE COLETA')
    moldura.inferiorDuplo()
    for m in coletas['pontos']:
        for k in escolhidos:
            if (k in m['aceita'] or k == 'tudo'):
                imprime.frase('')
                imprime.frase('')
                imprime.frase(m['nome'])
                for k in m['aceita']:
                    imprime.frase(' • ' + k)
                imprime.frase('')
                imprime.frase(' Latitude: ' + str(m['coordenadas'][0]))
                imprime.frase(' Longitude: ' + str(m['coordenadas'][1]))

def adicionarponto(nome, reclicaveis, coords, pontos):
    print(type(pontos))
    data = pontos
    data['pontos'].append({
        'nome' : nome,
        'coordenadas' : str(coords)
    })
    for i in reciclaveis:
        data['pontos'].aceita.append(i)
    with open('data/pontos_coleta.json', 'w', encoding="utf-8") as f:
        json.dump(pontos, f, ensure_ascii=False)

#parte temporaria para testes
#pega dados do json
with open('data/pontos_coleta.json', encoding='utf-8') as x:
    teste = json.load(x)

#tenta adicionar dados no json com a função acima.=
adicionarponto('Testando', ["metal","plastico"], [1,2], teste)
#parte temporaria para testes