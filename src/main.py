from jogadores import jogadores
from ordenacao import mergeSort


def contaInversoes(lista, tam, tipo: str):

    # Lista temporária que receberá
    # os jogadores durante a ordenação
    lista_temp = [{
        "id": 0,
        "nome": "",
        "rkng2000": 0,
        "rkngContemp": 0,
        "rkng90-": 0,
    }] * tam

    return mergeSort(lista, lista_temp,
                     0, tam - 1, tipo)


def contaEpoca(lista):
    """
    Analisa qual a época dos jogadores que aparecem mais
    no Top 5 do usuário.
    """

    from statistics import multimode, mode

    e = [x["epoca"] for x in lista]

    if len(multimode(e)) > 1:
        return 'unico'

    if mode(e) == 1:
        return 'rkng90-'
    elif mode(e) == 2:
        return 'rkng2000'
    elif mode(e) == 3:
        return 'rkngContemp'


print('-=' * 35)
msg = 'Bem-vindo(a) ao Melhores Jogadores !'
print(f'{msg:^70}')
print('-=' * 35)

for n in range(10):
    print(f'{n + 1:<2} - {jogadores[n]["nome"]:<20} \
{n + 11:<2} - {jogadores[n + 10]["nome"]:<20} \
{n + 21:<2} - {jogadores[n + 20]["nome"]:<20}')

print('-' * 50)
print('Escolha 5 atacantes dentre 30 os acima para formar o seu Top 5\n'
      'melhores atacantes do futebol. (em ordem do primeiro ao último)')
print('\nAo final descubra com qual estilo sua escolha se parece mais!')
print('-' * 30)

listaUsuario = list()
escolhido = []
pos = 0

while pos < 5:
    try:
        num = int(input(f'Escolha o {pos + 1}° jogador (número): '))

        if num not in range(1, 31):
            raise ValueError

        if num not in escolhido:
            escolhido.append(num)
        else:
            raise AssertionError

        for jogador in jogadores:
            if jogador["id"] == num:
                listaUsuario.append(jogador)
        print(f'Escolheu {listaUsuario[pos]["nome"]}.')
        pos += 1

    except ValueError:
        print('!! Informe um número válido !!')

    except AssertionError:
        print('!! Esse jogador já foi selecionado !!')

tam = len(listaUsuario)

tipoRanking = contaEpoca(listaUsuario)

epocas = {"rkng2000": 'Anos 2000',
          "rkngContemp": 'Anos 2010+',
          "rkng90-": 'Década de 90 (e antes)'}

print('-' * 30)
if tipoRanking not in ['rkng2000', 'rkngContemp', 'rkng90-']:
    print('Legal, você tem um estilo único!\nTem jogadores de várias épocas aí hein.\n')

    ordem = [n["nome"] for n in listaUsuario]
    print(f'Esta é a ordem do seu Top 5:\n{ordem}')

    lista1 = listaUsuario.copy()
    i1 = contaInversoes(lista1, tam, 'rkng2000')
    ordem1 = [n["nome"] for n in lista1]
    print(f'\nSeu Top 5 com base no ranking dos anos 2000:\n{ordem1} -> Qtd de inversões: {i1}')

    lista2 = listaUsuario.copy()
    i2 = contaInversoes(lista2, tam, 'rkngContemp')
    ordem2 = [n["nome"] for n in lista2]
    print(f'\nSeu Top 5 com base no ranking dos anos mais recentes:\n{ordem2} -> Qtd de inversões: {i2}')

    lista3 = listaUsuario.copy()
    i3 = contaInversoes(lista3, tam, 'rkng90-')
    ordem3 = [n["nome"] for n in lista3]
    print(f'\nSeu Top 5 com base no ranking anos 90:\n{ordem3} -> Qtd de inversões: {i3}')

else:
    print(f'Você tem um estilo mais perecido com \
a seguinte época: {epocas[tipoRanking]}')

    lista_aux = listaUsuario.copy()
    inv = contaInversoes(lista_aux, tam, tipoRanking)

    nomes = [n["nome"] for n in listaUsuario]
    print(f'\nEsta é a ordem do seu Top 5:\n{nomes}')

    nomes = [n["nome"] for n in lista_aux]
    print(f'\nSeu Top 5 com base no ranking dessa época ficaria assim:\n{nomes} -> Qtd de inversões: {inv}')

print('-' * 30)
