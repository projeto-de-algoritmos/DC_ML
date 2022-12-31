from jogadores import jogadores


def contaInversoes(lista, tam):
    ```
    Função que retorna um dicionário com a lista ordenada
    crescente para cada tipo de pontuação e a quantidade de
    inversões realizadas para a ordenação
    ```
    # Lista temporária que receberá
    # os jogadores durante a ordenação
    lista_temp = [{
        "id": 0,
        "nome": "",
        "ptsFIFA": 0,
        "ptsEnzo": 0,
        "ptsRetro": 0,
    }] * tam

    # Listas que receberam
    # a lista final ordenada, de acordo com o tipo de pontuação,
    # preservando a lista original.
    lista_fifa = lista.copy()
    lista_enzo = lista.copy()
    lista_retro = lista.copy()

    
    # Para cada tipo de pontuação, a lista será organizada,
    # E retornará um número de inversões (comparações)
    inversoes_fifa = mergeSort(lista_aux, lista_temp, 0, tam - 1, "ptsFIFA")
    inversoes_enzo = mergeSort(lista_aux, lista_temp, 0, tam - 1, "ptsEnzo")
    inversoes_retro = mergeSort(lista_aux, lista_temp, 0, tam - 1, "ptsRetro")


    return {
        "fifa": {"lista": lista_fifa, "inversoes": inversoes_fifa},
        "enzo": {"lista": lista_enzo, "inversoes": inversoes_enzo},
        "retro": {"lista": lista_retro, "inversoes": inversoes_retro},
    }


def mergeSort(lista, lista_temp, left, right, tipo_pts):
    ct_inversoes = 0

    # Realiza a recursão apenas se a lista tiver
    # mais de um elemento
    if left < right:
        # Valor para o índice que indica o meio da lista
        meio = (left + right) // 2

        # Chamada para a primeira metade da lista
        ct_inversoes += mergeSort(lista, lista_temp,
                                  left, meio, tipo_pts)

        # Chamada para a segunda metade da lista
        ct_inversoes += mergeSort(lista, lista_temp,
                                  meio + 1, right, tipo_pts)

        # Junção das metades
        ct_inversoes += merge(lista, lista_temp,
                              left, meio, right, tipo_pts)
    return ct_inversoes


def merge(lista, lista_temp, left, meio, right, tipo_pts):
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

        if lista[i][tipo_pts] <= lista[j][tipo_pts]:  # Não ocorreu inversão
            # compara com base no tipo de ponto de cada jogador

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
inversoes_e_listas = contaInversoes(listaUsuario, tam)

print('-' * 30)
print("Sua lista organizada por pontos FIFA:", inversoes_e_listas["fifa"]["lista"])
print("Número total de inversões por pontos FIFA:", inversoes_e_listas["fifa"]["inversoes"])
print("Sua lista organizada por pontos ENZO", inversoes_e_listas["enzo"]["lista"])
print("Número total de inversões por pontos ENZO:", inversoes_e_listas["enzo"]["inversoes"])
print("Sua lista organizada por pontos Retro:", inversoes_e_listas["retro"]["lista"])
print("Número total de inversões por pontos Retro:", inversoes_e_listas["retro"]["inversoes"])
