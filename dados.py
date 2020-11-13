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

def adicionarponto(pontos):

    coords = []
    moldura.superior()
    imprime.frase('ADICIONAR PONTO DE COLETA')
    imprime.frase('')
    imprime.frase('ATENÇÃO! Não utilize acentos!')
    moldura.inferior()
    nome = str(input('Digite o nome do local: '))
    print('')
    print('Digite como abaixo, sem espaços e somente os reciclaveis que o local aceita.')
    print('metal,plastico,vidro,papel,oleo,eletronico,madeira,borracha,isopor')
    rec = str(input('Digite os reciclaveis que o local aceita: '))
    reciclaveis = rec.split(',')
    print('')
    coords.append(float(input('Digite a latitude: ')))
    coords.append(float(input('Digite a longitude: ')))
    print('')
    data = pontos
    data['pontos'].append({
        'nome' : nome,
        'aceita' : reciclaveis,
        'coordenadas' : coords
    })
    with open('data/pontos_coleta.json', 'w') as outfile:
        json.dump(data, outfile, indent=4)

    moldura.superior()
    imprime.frase('PONTO ADICIONADO!')
    moldura.inferior()

def adicionarpontomassa(pontos):
    data = pontos
    qtde = 0
    moldura.superior()
    imprime.frase('ADICIONAR PONTOS DE COLETA EM MASSA')
    imprime.frase('')
    imprime.frase('ATENÇÃO! Não utilize acentos!')
    imprime.frase('Faça como no exemplo abaixo e seus deados serão todos adicionados!')
    imprime.frase('nome do local;metal,papel;-58.2345,-47.4839/nome do local;metal,plastico;-58.2345,-47.4839')
    imprime.frase('')
    imprime.frase("Preste atenção que se utiliza ';' entre os dados e '/' entre pontos diferentes")
    imprime.frase('Utilize espaços SOMENTE no nome do local e use o padrão correto para digitar as coordenadas')
    imprime.frase('')
    imprime.frase('Reciclaveis válidos: metal, plastico, papel, vidro, borracha, oleo, eletronico, madeira e isopor')
    moldura.inferior()
    lista = input('Digite a seguir a sua lista de pontos: ')
    dados = lista.split('/')

    for i in dados:
        ponto = i.split(';')
        ponto[1] = ponto[1].split(',')
        ponto[2] = ponto[2].split(',')
        data['pontos'].append({
            'nome' : ponto[0],
            'aceita' : ponto[1],
            'coordenadas' : ponto[2]
        })
        qtde += 1

    with open('data/pontos_coleta.json', 'w') as outfile:
        json.dump(data, outfile, indent=4)

    moldura.superior()
    imprime.frase(str(qtde) + ' PONTOS ADICIONADO!')
    moldura.inferior()