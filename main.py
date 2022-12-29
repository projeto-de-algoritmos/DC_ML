from jogadores import jogadores


print('-=' * 20)
print('  Bem-vindo(a) ao Melhores Jogadores !')
print('-=' * 20)

for n, v in enumerate(jogadores):
    print(f'{n + 1:<2} - {v["nome"]}')

print('-' * 20)
print('Escolha 5 atacantes dentre os acima para formar o seu Top 5\n'
      'melhores atacantes do futebol. (em ordem do primeiro ao último)')
print('-' * 30)

listaUsuario = list()
escolhido = []
pos = 0

while pos < 5:
    try:
        num = int(input(f'Escolha o {pos+1}° jogador (número): '))

        if num not in range(1, 21):
            raise ValueError

        if num not in escolhido:
            escolhido.append(num)
        else:
            raise AssertionError

        for jogador in jogadores:
            if jogador["id"] == num:
                listaUsuario.append(jogador)

        pos += 1

    except ValueError:
        print('!! Informe um número válido !!')

    except AssertionError:
        print('Esse jogador já foi selecionado.')

print('-'*30)
print('Este é o seu Top 5 melhores atacantes:')

for n, v in enumerate(listaUsuario):
    print(f'{n+1}°- {v["nome"]}', end='; ')
