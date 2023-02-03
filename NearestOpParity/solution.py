from sys import stdin,stdout
from collections import deque


n = int(stdin.readline())

a = list(map(int,stdin.readline().split()))

evens, odds = [],[]

ady = [[] for i in range(n)]

sol = ['-1' for i in range(n)]


for i in range(n):
    ai = a[i]
    l = i-ai
    r = i+ai
    if l >= 0:
        ady[l].append(i)
    if r < n:
        ady[r].append(i)
    if ai%2 == 0:
        evens.append(i)
    else:
        odds.append(i)

def BFS(red,blue):
    d = [-1 for i in range(n)]
    q = deque()
    for u in red:
        d[u] = 0
        q.append(u)
    while len(q)>0:
        v = q.popleft()
        for i in ady[v]:
            if d[i] == -1:
                d[i] = d[v] + 1
                q.append(i)
    for i in blue:
        if d[i] != -1:
            sol[i] = str(d[i])

BFS(evens,odds)
BFS(odds,evens)
stdout.write(' '.join(sol))
