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
