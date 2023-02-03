from utils import *
import random as rand

def generator(path : str, nodes : int, edges : int) -> None:
    # abrimos el archivo
    file = open_file(path)

    # generamos y exportamos el grafo
    file.write('%d %d\n'%(nodes, edges))
    graph = [set() for _ in range(nodes + 5)]
    i = 0

    while i < edges:
        u, v = rand.randint(1, nodes), rand.randint(1, nodes)
        if u != v and not contain_edge(graph, u, v):
            file.write('%d %d\n'%(u, v))
            graph[u].add(v)
            graph[v].add(u)
            i += 1

    # cerramos el archivo
    file.close()
    print(f'{path} completed')

def main():
    # generator('../Casos de prueba (mio)/caso17.in', 80, 150)
    # generator('../Casos de prueba (mio)/caso18.in', 100, 300)
    # generator('../Casos de prueba (mio)/caso19.in', 250, 500)
    # generator('../Casos de prueba (mio)/caso20.in', 350, 700)
    # generator('../Casos de prueba (mio)/caso21.in', 400, 800)
    # generator('../Casos de prueba (mio)/caso22.in', 500, 1000)
    # generator('../Casos de prueba (mio)/caso23.in', 750, 1500)
    # generator('../Casos de prueba (mio)/caso24.in', 1000, 2000)
    # generator('../Casos de prueba (mio)/caso25.in', 100000, 100000)
    
if __name__ == '__main__':
    main()
