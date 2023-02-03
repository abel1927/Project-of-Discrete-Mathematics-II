from sys import stdin, stdout
from heapq import heapify,heappop,heappush
 
n, m = map(int, stdin.readline().split())
 
ady = [[] for i in range(n)]
 
for i in range(m):
    u,v,w = map(int,stdin.readline().split())
    ady[u-1].append((v-1,2*w))
    ady[v-1].append((u-1,2*w))
 
c_xcity = list(map(int,stdin.readline().split()))
pq = [(c_xcity[i],i) for i in range(n)]
heapify(pq)
while len(pq)>0:
    wu,u = heappop(pq)
    if c_xcity[u] != wu:
        continue
    for v,w in ady[u]:
        if c_xcity[v] > c_xcity[u] + w:
            c_xcity[v] = c_xcity[u] + w
            heappush(pq,(c_xcity[v],v))
 
stdout.write(' '.join(map(str,c_xcity)))
