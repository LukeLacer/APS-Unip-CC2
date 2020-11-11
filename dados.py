import json #modulo que gerencia o json
import moldura, imprime

#pega o json e joga no dicionario dados_reciclaveis
with open('data/pontos_coleta.json', encoding="utf8") as f:
    pontos = json.load(f)

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

def reciclaveis(coletas, materiais):
    for p in coletas['pontos']: