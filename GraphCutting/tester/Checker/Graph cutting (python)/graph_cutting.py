import os

def partition(output_file : str, graph, u : int) -> int:
    aux = []

    while len(graph[u]) != 0:
        v = graph[u].pop()
        graph[v].remove(u)
        node = partition(output_file, graph, v)

        if node != -1:
            output_file.write(f'{u} {v} {node}\n')
        else:
            aux.append(v)

    for i in range(len(aux) % 2, len(aux), 2):
        output_file.write(f'{aux[i]} {u} {aux[i + 1]}\n')

    if len(aux) % 2 == 1:
        return aux[0]
    else:
        return -1

def graph_cutting(input_file : str, output_file : str) -> None:
    import time
    first_time = time.time()

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

    if edges % 2 == 1:
        output_file.write('No solution\n')
    else:
        partition(output_file, graph, 1)

    second_time = time.time()
    time = second_time - first_time
    output_file.write(f'{time}\n')

def main():

    for file in os.listdir('./tests/'):
        name, extention = os.path.splitext(file)

        if extention == '.out':
            input_file = open('./tests/' + name + '.in', 'r')
            output_file = open('./tests/' + file, 'w')

            graph_cutting(input_file, output_file)
            print(f'{name} completed')

            input_file.close()
            output_file.close()
            
    print('DONE')

if __name__ == "__main__":
    main()