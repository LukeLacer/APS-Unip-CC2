#cria borda superior com uma linha abaixo
def superior():
    print('┌' + '─' * 100 + '┐')
    print('│' + ' ' * (100) + '│')

#cria borda inferior com uma linha acima
def inferior():
    print('│' + ' ' * (100) + '│')
    print('└' + '─' * 100 + '┘')

def superiorDuplo():
    print('│' + ' ' * (100) + '│')

#cria borda inferior com uma linha acima
def inferiorDuplo():
    print('│' + ' ' * (100) + '│')
    print('╞' + '═' * 100 + '╡')

#cria borda de 100x25 no interior dela
def default():
    superior()
    for _ in range(25-2):
        print('│' + ' ' * (100) + '│')
    inferior()