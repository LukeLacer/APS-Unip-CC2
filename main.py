import json #modulo que gerencia o json
import dados, moldura, imprime

#pega o json e joga no dicionario dados_reciclaveis
with open('data/dados_reciclaveis.json', encoding="utf8") as f:
    dados_reciclaveis = json.load(f)

#pega o json e joga no dicionario pontos
with open('data/pontos_coleta.json', encoding="utf8") as f:
    pontos = json.load(f)

imprime.titulo()
imprime.entrada()

#menu (escolhas do menu)
escolha = 50
while (int(escolha) != 0):
    imprime.menu()
    escolha = input('Digite a opção desejada: ')
    if (int(escolha) == 1):
        dados.reciclaveis(dados_reciclaveis, 'metal')
        escolha = imprime.opcao1()
    elif (int(escolha) == 2):
        dados.reciclaveis(dados_reciclaveis, 'plastico')
        escolha = imprime.opcao1()
    elif (int(escolha) == 3):
        dados.reciclaveis(dados_reciclaveis, 'papel')
        escolha = imprime.opcao1()
    elif (int(escolha) == 4):
        dados.reciclaveis(dados_reciclaveis, 'vidro')
        escolha = imprime.opcao1()
    elif (int(escolha) == 5):
        dados.reciclaveis(dados_reciclaveis, 'isopor')
        escolha = imprime.opcao1()
    elif (int(escolha) == 6):
        dados.reciclaveis(dados_reciclaveis, 'madeira')
        escolha = imprime.opcao1()
    elif (int(escolha) == 7):
        dados.reciclaveis(dados_reciclaveis, 'borracha')
        escolha = imprime.opcao1()
    elif (int(escolha) == 8):
        dados.reciclaveis(dados_reciclaveis, 'oleo')
        escolha = imprime.opcao1()
    elif (int(escolha) == 9):
        dados.reciclaveis(dados_reciclaveis, 'eletronico')
        escolha = imprime.opcao1()
    elif (int(escolha) == 11):
        #ponto de coleta mais próximo
        escolha = imprime.opcao1()
    elif (int(escolha) == 12):
        dados.pontosraio(pontos)
        escolha = imprime.opcao1()
    elif (int(escolha) == 13):
        #ver todos os pontos
        escolha = imprime.opcao1()
    elif (int(escolha) == 14):
        #adicionar ponto de coleta
        escolha = imprime.opcao1()
    elif (int(escolha) == 15):
        #adicionar ponto de coleta em massa
        escolha = imprime.opcao1()