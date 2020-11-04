import moldura

#escreve o titulo do programa na tela
def titulo():
    moldura.default_superior()
    print('│ ' + ' ' * 25 + '███  ███  ███  █  ███  █    ███  █ █  ███  █  ███' + ' ' * 25 + '│')
    print('│ ' + ' ' * 25 + '█ █  █    █    █  █    █    █ █  █ █  █    █  █  ' + ' ' * 25 + '│')
    print('│ ' + ' ' * 25 + '██   ███  █    █  █    █    ███  █ █  ███  █  ███' + ' ' * 25 + '│')
    print('│ ' + ' ' * 25 + '█ █  █    █    █  █    █    █ █  █ █  █    █    █' + ' ' * 25 + '│')
    print('│ ' + ' ' * 25 + '█ █  ███  ███  █  ███  ███  █ █   █   ███  █  ███' + ' ' * 25 + '│')
    moldura.default_inferior()

def texto(texto):
    vet = texto.split()
    resultado = []
    linha = ''
    for i in vet:
        if (len(linha) + len(i) + 1 < 98) :
            if linha == '':
                linha += i
            else:
                linha += ' ' + i
        else:
            resultado.append(linha)
            linha = ''
            linha += i
    resultado.append(linha)

    #imprime o texto
    for i in resultado:
        print('│ ' + i + ' ' * (98 - len(i)) + ' │')

texto('No Brasil, 98% de todas as latas de alumínio vão parar na indústria vindo da coleta de reciclagem, custando 5% do valor de fabricação de uma lata advinda da extração da natureza. Aço, alumínio, cobre, estanho e zinco são os principais metais recicláveis, porém é importante falar que clipes e grampos, esponjas e palhas de aço, latas de aerossóis, latas de tintas, vernizes e solventes, latas de produtos tóxicos como inseticidas e pesticidas, produtos feitos com metais pesados, inclusive pilhas, baterias e tomadas não sao recicláveis. Pilhas, bateriais e outros produtos com metal pesado devem ainda ser descartados em pontos de coelta especiais.')