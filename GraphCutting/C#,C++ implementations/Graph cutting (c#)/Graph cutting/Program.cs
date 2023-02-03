using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Graph_cutting
{
    class Program
    {
        static int Particionar(SortedSet<int>[] grafo, int u)
        {
            List<int> aux = new List<int>();

            while (grafo[u].Count != 0)
            {
                int v = grafo[u].Min;
                grafo[u].Remove(v);
                grafo[v].Remove(u);
                int nodo = Particionar(grafo, v);

                if (nodo != -1)
                    Console.WriteLine("{0} {1} {2}", u, v, nodo);
                else
                    aux.Add(v);
            }

            for (int i = (aux.Count() % 2); i < aux.Count(); i += 2)
            {
                Console.WriteLine("{0} {1} {2}", aux[i], u, aux[i + 1]);
            }

            if (aux.Count() % 2 == 1)
                return aux[0];
            else
                return -1;
        }

        static void Main(string[] args)
        {
            string[] linea = Console.ReadLine().Split();
            int vertives = int.Parse(linea[0]);
            int aristas = int.Parse(linea[1]);

            SortedSet<int>[] grafo = new SortedSet<int>[aristas + 5];
            for (int i = 0; i < grafo.Length; i++)
            {
                grafo[i] = new SortedSet<int>();
            }

            for (int i = 0; i < aristas; i++)
            {
                linea = Console.ReadLine().Split();
                int u = int.Parse(linea[0]);
                int v = int.Parse(linea[1]);

                grafo[u].Add(v);
                grafo[v].Add(u);
            }

            if (aristas % 2 == 1)
                Console.WriteLine("No solution");
            else
                Particionar(grafo, 1);
        }
    }
}
