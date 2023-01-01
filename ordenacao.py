def mergeSort(lista, lista_temp, left, right, tipo):
    ct_inversoes = 0

    # Realiza a recursão apenas se a lista tiver
    # mais de um elemento
    if left < right:
        lista_nada = []
        # Valor para o índice que indica o meio da lista
        meio = (left + right) // 2

        # Chamada para a primeira metade da lista
        ct_inversoes += mergeSort(lista, lista_temp,
                                  left, meio, tipo)

        # Chamada para a segunda metade da lista
        ct_inversoes += mergeSort(lista, lista_temp,
                                  meio + 1, right, tipo)

        # Junção das metades
        ct_inversoes += merge(lista, lista_temp,
                              left, meio, right, tipo)

    return ct_inversoes


def merge(lista, lista_temp, left, meio, right, tipo):
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

        if lista[i][tipo] <= lista[j][tipo]:  # Não ocorreu inversão
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

    # Cópia dos elementos the sorted subarray into
    # Original array

    for loop_var in range(left, right + 1):
        # fazer retornar essa lista para o usuário poder ver também
        lista[loop_var] = lista_temp[loop_var]

    return ct_inversoes
