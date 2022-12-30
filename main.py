from jogadores import jogadores


def contaInversoes(lista, tam):
    # Lista temporária que receberá
    # os jogadores durante a ordenação
    lista_temp = [{
        "id": 0,
        "nome": "",
        "ptsFIFA": 0,
        "ptsEnzo": 0,
        "ptsRetro": 0,
    }] * tam

    # Lista auxiliar que receberá
    # a lista final ordenada,
    # preservando a lista original.
    lista_aux = lista.copy()

    return mergeSort(lista_aux, lista_temp,
                     0, tam - 1)


def mergeSort(lista, lista_temp, left, right):
    ct_inversoes = 0

    # Realiza a recursão apenas se a lista tiver
    # mais de um elemento
    if left < right:
        # Valor para o índice que indica o meio da lista
        meio = (left + right) // 2

        # Chamada para a primeira metade da lista
        ct_inversoes += mergeSort(lista, lista_temp,
                                  left, meio)

        # Chamada para a segunda metade da lista
        ct_inversoes += mergeSort(lista, lista_temp,
                                  meio + 1, right)

        # Junção das metades
        ct_inversoes += merge(lista, lista_temp,
                              left, meio, right)
    return ct_inversoes


def merge(lista, lista_temp, left, meio, right):
    # Iterador para a primeira metade
    i = left

    # Iterador para a segunda metade
    j = meio + 1

    # Iterador para a lista temporária
    # que será ordenada
    k = left

    ct_inversoes = 0

    # Garante que as comparações entre as metades
    # e a contagem de inversões serão interrompidos,
    # caso i ou j excedam o limite de cada lista
    while i <= meio and j <= right:

        if lista[i]["ptsFIFA"] <= lista[j]["ptsFIFA"]:  # Não ocorreu inversão
            # compara com base nos pontos FIFA de cada jogador

            # Só o elemento da primeira metade é inserido
            lista_temp[k] = lista[i]
            k += 1
            i += 1
        else:
            # Só o elemento da segunda metade é inserido
            # e ocorre a contagem geral das inversões
            lista_temp[k] = lista[j]
            ct_inversoes += (meio - i + 1)
            k += 1
            j += 1

    # Insere na lista temporária os elementos restantes
    # da primeira metade caso o iterador j tenha excedido
    # seu limite
    while i <= meio:
        lista_temp[k] = lista[i]
        k += 1
        i += 1

    # Insere na lista temporária os elementos restantes
    # da segunda metade caso o iterador i tenha excedido
    # seu limite
    while j <= right:
        lista_temp[k] = lista[j]
        k += 1
        j += 1

    return ct_inversoes


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
        num = int(input(f'Escolha o {pos + 1}° jogador (número): '))

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
        print('!! Esse jogador já foi selecionado !!')

tam = len(listaUsuario)
inversoes = contaInversoes(listaUsuario, tam)

print('-' * 30)
print("Número total de inversões:", inversoes)
