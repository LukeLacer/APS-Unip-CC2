import moldura

#escreve o titulo do programa na tela
def titulo():
    moldura.superior()
    print('│ ' + ' ' * 25 + '███  ███  ███  █  ███  █    ███  █ █  ███  █  ███' + ' ' * 25 + '│')
    print('│ ' + ' ' * 25 + '█ █  █    █    █  █    █    █ █  █ █  █    █  █  ' + ' ' * 25 + '│')
    print('│ ' + ' ' * 25 + '██   ███  █    █  █    █    ███  █ █  ███  █  ███' + ' ' * 25 + '│')
    print('│ ' + ' ' * 25 + '█ █  █    █    █  █    █    █ █  █ █  █    █    █' + ' ' * 25 + '│')
    print('│ ' + ' ' * 25 + '█ █  ███  ███  █  ███  ███  █ █   █   ███  █  ███' + ' ' * 25 + '│')
    print('╞' + '═' * 100 + '╡')

def texto(texto):

    #separa o texto em linhas para não ultrapassar o espaço da interface
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

def frase(texto):
    #imprime a frase
    print('│ ' + texto + ' ' * (98 - len(texto)) + ' │')

def entrada():
    texto('Olá! Esse software foi criado como projeto semestral acadêmico com o intuito de difundir o conhecimento sobre materiais reciclaveis e seus pontos de coleta!')
    texto('')
    texto('Universidade Paulista - UNIP - Campinas Campus II')
    texto('Disciplina: Atividades Práticas Supervisionadas (APS)')
    texto('Professor: Celso Aimbiré Weffort-Santos')
    texto('')
    texto('Alunos:')
    texto('F3082B2 - GIULIO CESAR PEREIRA PIMENTA')
    texto('F2662C6 - LUCAS LACERDA DE LIMA')
    texto('N578980 - LUCAS PEREZ LIMA')
    texto('N6285G9 - MATEUS FAGNANI MARTINS')
    texto('N578GC0 - MATHEUS QUEIROZ OLIVEIRA')
    moldura.inferior()


def menu():
    moldura.superior()
    texto('MENU')
    texto('')
    texto('Aqui você pode escolher uma opção para navegar pelo programa. Basta digitar a opção que deseja e apertar Enter.')
    texto('')
    texto('>> Saber mais sobre os materiais reciclaveis')
    frase('    1 - Metal')
    frase('    2 - Plástico')
    frase('    3 - Papel')
    frase('    4 - Vidro')
    frase('    5 - Isopor')
    frase('    6 - Madeira')
    frase('    7 - Borracha')
    frase('    8 - Óleo de cozinha')
    frase('    9 - Lixo Eletrônico')
    texto('>> Dados dos pontos de coleta')
    frase('   11 - Ver ponto de coleta mais próximo por material que coleta')
    frase('   12 - Ver pontos de coleta num raio por material que coleta')
    frase('   13 - Ver todos os pontos de coleta por material que coleta')
    frase('   14 - Adicionar ponto de coleta')
    frase('   15 - Adicionar pontos de coleta em massa')
    texto('')
    frase('    0 - Sair do programa')
    moldura.inferior()