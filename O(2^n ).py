def mochila(itens, capacidade):
    if len(itens) == 0 or capacidade == 0:
        return 0

    peso, valor = itens[0]
    if peso > capacidade:
        return mochila(itens[1:], capacidade)
    else:
        return max(mochila(itens[1:], capacidade),
                   valor + mochila(itens[1:], capacidade - peso))

