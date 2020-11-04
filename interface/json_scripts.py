import json #modulo que gerencia o json
import imprime

#pega o json e joga no dicionario dados_reciclaveis
with open('data/dados_reciclaveis.json', encoding="utf8") as f:
    dados_reciclaveis = json.load(f)

#percorre o dicionario imprimindo TODOS os dados
def reciclaveis(data):
    for p in data['reciclaveis']:
        print(p['material'].upper())
        print('Tereciclaveismpo de Degradação: ' + p['tempo_degradacao'])
        print('')
        imprime.texto(p['resumo'])
        print('')
        print('PODEMOS RECICLAR:')
        for i in p['reciclaveis']:
            print('✔  ' + i)
        print('')
        print('NÃO PODEMOS RECICLAR:')
        for i in p['nao_reciclaveis']:
            print('✘  ' + i)
        print('')
        print('------------------------------------------------------------------------------------')
        print('')
#fim_reciclaveis

    '''
    imprime somente o metal
    for p in data['reciclaveis']:
        if p['material'] == 'metal':
            print(p)
    '''

reciclaveis(dados_reciclaveis)