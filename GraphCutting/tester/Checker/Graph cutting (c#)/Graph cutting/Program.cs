using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Graph_cutting
{
    class Program
    {
        static int Partition(StreamWriter output_file, SortedSet<int>[] graph, int u)
        {
            List<int> aux = new List<int>();

            while (graph[u].Count != 0)
            {
                int v = graph[u].Min;
                graph[u].Remove(v);
                graph[v].Remove(u);
                int node = Partition(output_file, graph, v);

                if (node != -1)
                    output_file.WriteLine("{0} {1} {2}", u, v, node);
                else
                    aux.Add(v);
            }

            for (int i = (aux.Count() % 2); i < aux.Count(); i += 2)
            {
                output_file.WriteLine("{0} {1} {2}", aux[i], u, aux[i + 1]);
            }

            if (aux.Count() % 2 == 1)
                return aux[0];
            else
                return -1;
        }

        static void GraphCutting(StreamReader input_file, StreamWriter output_file)
        {
            Stopwatch crono = new Stopwatch();
            crono.Start();

            string[] line = input_file.ReadLine().Split();
            int nodes = int.Parse(line[0]);
            int edges = int.Parse(line[1]);

            SortedSet<int>[] graph = new SortedSet<int>[nodes + 5];
            for (int i = 0; i < graph.Length; i++)
            {
                graph[i] = new SortedSet<int>();
            }

            for (int i = 0; i < edges; i++)
            {
                line = input_file.ReadLine().Split();
                int u = int.Parse(line[0]);
                int v = int.Parse(line[1]);

                graph[u].Add(v);
                graph[v].Add(u);
            }

            if (edges % 2 == 1)
                output_file.WriteLine("No solution");
            else
                Partition(output_file, graph, 1);

            crono.Stop();
            double time = crono.ElapsedMilliseconds / 1000.0;
            output_file.WriteLine(time);
        }

        static void Main(string[] args)
        {
            for (int i = 1; i <= 24; i++)
            {
                StreamReader input_file = File.OpenText("tests/caso" + i.ToString() + ".in");
                StreamWriter output_file = File.CreateText("tests/caso" + i.ToString() + ".out");

                GraphCutting(input_file, output_file);
                Console.WriteLine("tests/caso" + i.ToString() + " completed");

                input_file.Close();
                output_file.Close();
            }

            Console.WriteLine("DONE");
        }
    }
}
