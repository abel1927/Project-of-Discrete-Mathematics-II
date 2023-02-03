import os
from colorama import init, Fore

def is_edge(graph : list, u : int, v : int) -> bool:
    return graph[u].__contains__(v) and graph[v].__contains__(u)

def is_null(graph : list) -> bool:
    for i in graph:
        if len(i) != 0:
            return False
    return True

def get_veredict(graph : list, nodes : int, edges : int, output_file) -> str:
    lines = output_file.readlines()
    
    if edges % 2 == 1:
        if (len(lines) - 1) != 1:
            return 'WRONG ANSWER'

        line = lines[0].split('\n')[0]
        time = float(lines[len(lines) - 1])
        if line != 'No solution':
            return 'WRONG ANSWER'
        elif time > 2.0:
            return 'TIME LIMIT EXCEDED'
        else:
            return 'ACCEPTED'
    else:
        if (len(lines) - 1) != (edges // 2):
            return 'WRONG ANSWER'
        
        for i in range(len(lines) -1):
            line = lines[i].split()
            if len(line) != 3:
                return 'WRONG ANSWER'

            a, b, c = int(line[0]), int(line[1]), int(line[2])
            if a <= 0 or a > 100000 or b <= 0 or b > 100000 or c <= 0 or c > 100000:
                return 'WRONG ANSWER'
            elif not is_edge(graph, a, b) or not is_edge(graph, b, c):
                return 'WRONG ANSWER'
            
            graph[a].remove(b)     # eliminamos la arista <a, b>
            graph[b].remove(a)
            graph[b].remove(c)     # eliminamos la arista <b, c>
            graph[c].remove(b)

        if not is_null(graph):
            return 'WRONG ANSWER'
        elif float(lines[len(lines) - 1]) > 2.0:
            return 'TIME LIMIT EXCEDED'
        else:
            return 'ACCEPTED'

def build_graph(input_file) -> list:
    line = input_file.readline().split()
    nodes = int(line[0])
    edges = int(line[1])

    graph = [set() for _ in range(nodes + 5)]

    for i in range(edges):
        line = input_file.readline().split()
        u = int(line[0])
        v = int(line[1])

        graph[u].add(v)
        graph[v].add(u)

    return graph, nodes, edges

def checker(path_cases : str) -> None:
    acc, wa, tle, total = 0, 0, 0, 0
    init(autoreset=True)

    for file in os.listdir(path_cases):
        name, extention = os.path.splitext(file)
        if extention == '.out':
            input_file = open(path_cases + str(name) + '.in')
            output_file = open(path_cases + str(file))

            graph, nodes, edges = build_graph(input_file)
            solution = get_veredict(graph, nodes, edges, output_file)
            print(name, '->', end=' ')
            total += 1
            
            if solution == 'ACCEPTED':
                print(Fore.GREEN + solution)
                acc += 1
            elif solution == 'WRONG ANSWER':
                print(Fore.RED + solution)
                wa += 1
            else:
                print(Fore.BLUE + solution)
                tle += 1

    print(f'\nACEPTADOS: {acc}, FALLADOS: {wa}, LIMITE DE TIEMPO: {tle}, TOTAL: {total}')
    print('POR CIENTO DE ACEPTADOS: %0.2f\n'%(100 * acc / total))

def main() -> None:
    print('SELECIONE EL LENGUAJE QUE DESEA PROBAR')
    print('1. C++')
    print('2. C#')
    print('3. Python')

    option = int(input())

    if option <= 0 or option > 3:
        print('DEBE SELECCIONAR UN NUMERO ENTRE 1 Y 3 (AMBOS INCLUSIVOS).')
        return

    if option == 1:
        path_cases = './Graph cutting (c++)/tests/'
    elif option == 2:
        path_cases = './Graph cutting (c#)/Graph cutting/bin/Debug/tests/'
    else:
        path_cases = './Graph cutting (python)/tests/'

    checker(path_cases)
    
if __name__ == '__main__':
    main()
