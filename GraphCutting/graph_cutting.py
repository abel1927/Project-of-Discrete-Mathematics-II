def particionar(grafo, u):
    aux = []

    while(len(grafo[u]) != 0):
        v = grafo[u].pop()
        grafo[v].remove(u)
        nodo = particionar(grafo, v)

        if nodo != -1:
            print(f'{u} {v} {nodo}')
        else:
            aux.append(v)

    for i in range(len(aux) % 2, len(aux), 2):
        print(f'{aux[i]} {u} {aux[i + 1]}')

    if len(aux) % 2 == 1:
        return aux[0]
    else:
        return -1

def main():
    linea = input().split()
    vertices = int(linea[0])
    aristas = int(linea[1])

    grafo = [set() for _ in range(vertices + 5)]

    for i in range(aristas):
        linea = input().split()
        u = int(linea[0])
        v = int(linea[1])

        grafo[u].add(v)
        grafo[v].add(u)

    if aristas % 2 == 1:
        print("No solution")
    else:
        particionar(grafo, 1)

if __name__ == "__main__":
    main()