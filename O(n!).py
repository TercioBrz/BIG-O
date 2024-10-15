def permutacoes(lista):
    if len(lista) == 0:
        return [[]]
    
    resultado = []
    for i in range(len(lista)):
        restante = lista[:i] + lista[i+1:]
        for p in permutacoes(restante):
            resultado.append([lista[i]] + p)
    
    return resultado

# Exemplo de uso:
lista=[]
for _ in range(5):
    valor = input()
    lista.append(valor)
    
resultado = permutacoes(lista)
for p in resultado:
    print(p)
