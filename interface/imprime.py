import moldura

#escreve o titulo do programa na tela
def titulo():
    moldura.default_superior()
    print('| ' + ' ' * 25 + '███  ███  ███  █  ███  █    ███  █ █  ███  █  ███' + ' ' * 25 + '|')
    print('| ' + ' ' * 25 + '█ █  █    █    █  █    █    █ █  █ █  █    █  █  ' + ' ' * 25 + '|')
    print('| ' + ' ' * 25 + '██   ███  █    █  █    █    ███  █ █  ███  █  ███' + ' ' * 25 + '|')
    print('| ' + ' ' * 25 + '█ █  █    █    █  █    █    █ █  █ █  █    █    █' + ' ' * 25 + '|')
    print('| ' + ' ' * 25 + '█ █  ███  ███  █  ███  ███  █ █   █   ███  █  ███' + ' ' * 25 + '|')
    moldura.default_inferior()

def texto(texto):
    vet = texto.split()
    print(vet)