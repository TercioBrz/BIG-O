
def busca_binaria(lista, alvo):
    baixo = 0
    alto = len(lista) - 1

    while baixo <= alto:
        meio = (baixo + alto) // 2
        if lista[meio] == alvo:
            return True
        elif lista[meio] < alvo:
            baixo = meio + 1
        else:
            alto = meio - 1
    return False
