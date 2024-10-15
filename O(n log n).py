def merge_sort(lista):
    if len(lista) > 1:
        meio = len(lista) // 2
        esquerda = lista[:meio]
        direita = lista[meio:]

        merge_sort(esquerda)
        merge_sort(direita)

        i = j = k = 0

        # Merge das duas metades
        while i < len(esquerda) and j < len(direita):
            if esquerda[i] < direita[j]:
                lista[k] = esquerda[i]
                i += 1
            else:
                lista[k] = direita[j]
                j += 1
            k += 1

        # Copiar os elementos restantes de 'esquerda'
        while i < len(esquerda):
            lista[k] = esquerda[i]
            i += 1
            k += 1

        # Copiar os elementos restantes de 'direita'
        while j < len(direita):
            lista[k] = direita[j]
            j += 1
            k += 1

    return lista
