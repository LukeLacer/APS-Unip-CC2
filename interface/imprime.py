import moldura

#escreve o titulo do programa na tela
def titulo():
    print('| ' + '██     ██   ██ ██████ ██████ ██████' + ' ' * (100 - 36) + '|')
    print('| ' + '██     ██   ██ ██     ██  ██ ██    ' + ' ' * (100 - 36) + '|')
    print('| ' + '██     ██   ██ ██     ██  ██ ██    ' + ' ' * (100 - 36) + '|')
    print('| ' + '██     ██   ██ ██     ██████ ██████' + ' ' * (100 - 36) + '|')
    print('| ' + '██     ██   ██ ██     ██  ██     ██' + ' ' * (100 - 36) + '|')
    print('| ' + '██████ ███████ ██████ ██  ██ ██████' + ' ' * (100 - 36) + '|')

moldura.default_superior()
titulo()
moldura.default_inferior()