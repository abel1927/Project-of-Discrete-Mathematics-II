from sys import stdin,stdout
from math import log2, ceil

n,m = map(int, stdin.readline().split())

class Edge:
    def __init__(self,u,v,w,i):
        self.i = i
        self.u = u
        self.v = v
        self.w = w

E = []

ady = [[]for i in range(n)]

for i in range(m):
    u,v,w = map(int,stdin.readline().split())
    E.append(Edge(u-1,v-1,w,i))

edges = sorted(E, key=lambda e: e.w)

cc = n
parent = [i for i in range(n)]
rank = [0 for i in range(n)]

logN = ceil(log2(n))+1

wMST = 0

def setOf(x):
    if parent[x] == x:
        return x
    parent[x] = setOf(parent[x])
    return parent[x]

def Merge(x,y):
    if rank[x] > rank[y]:
        parent[y] = x
    elif rank[y] > rank[x]:
        parent[x] = y
    else:
        parent[x] = y
        rank[y] = rank[y]+1

for e in edges:
    if cc == 1:
        break
    x = setOf(e.u)
    y = setOf(e.v)
    if x != y:
        cc = cc-1
        Merge(x,y)
        wMST = wMST + e.w
        ady[e.u].append((e.v,e.w))
        ady[e.v].append((e.u,e.w))


dp = [[0 for i in range(logN)] for e in range(n)]

dw = [[0 for i in range(logN)] for e in range(n)]

level = [0 for i in range(n)] 

def dft(v, pv):
    dp[v][0] = pv
    for i in range(1,logN):
        if dp[v][i-1] == -1:
            dp[v][i] = -1
            dw[v][i] = -1
        else:
            dp[v][i] = dp[dp[v][i-1]][i-1]
            dw[v][i] = max(dw[v][i-1],dw[dp[v][i-1]][i-1])
    for e in ady[v]:
        u,w = e[0],e[1]
        if u == pv:
            continue
        level[u] = level[v]+1
        dw[u][0] = w
        dft(u,v)

def lca(u,v):
    if level[u]>level[v]:
        u,v = v,u
    max_edge = -1
    for i in range(logN,-1,-1):
		if lev[v] - 2**i >= lev[u]:
			max_edge = max(max_edge,dw[v][i])
			v = dp[v][i]	

    if u == v:
        return max_edge
    
	for i in range(logN,-1,-1):
		if dp[u][i]!=dp[v][i]:
			max_edge = max(max_edge,dw[u][i])
			max_edge = max(max_edge,dw[v][i])
			u = dp[u][i]
			v = dp[v][i]

    return max(max_edge, max(dw[v][0],dw[u][0]))    

dw[0][0] = -1
dft(0,-1)

ans = ['-1' for i in range(m)]

for e in edges:
    a = wMST - lca(e.u,e.v) + e.w
    ans[e.i] = str(a)

stdout.write('\n'.join(ans))
