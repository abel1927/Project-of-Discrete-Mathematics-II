#include<bits/stdc++.h>
#define endl '\n'

using namespace std;

set<int> grafo[100005];

int particionar(int u)
{
    vector<int> aux;

    while(grafo[u].size())
    {
        int v = *(grafo[u].begin());
        grafo[v].erase(u);
        grafo[u].erase(v);
        int nodo = particionar(v);

        if(nodo != -1)
            printf("%d %d %d\n", u, v, nodo);
        else
            aux.push_back(v);
    }

    for(int i = (aux.size() % 2); i < aux.size(); i += 2)
    {
        printf("%d %d %d\n", aux[i], u, aux[i + 1]);
    }

    if(aux.size() % 2 == 1)
        return aux[0];
    else
        return -1;
}

int main()
{
    ios_base :: sync_with_stdio(0);
    cin.tie(0);

    int vertices, aristas;
    scanf("%d %d", &vertices, &aristas);

    for(int i = 0; i < aristas; i++)
    {
        int u, v;
        scanf("%d %d", &u, &v);

        grafo[u].insert(v);
        grafo[v].insert(u);
    }

    if(aristas % 2 == 1)
        printf("No solution\n");
    else
        particionar(1);
}
