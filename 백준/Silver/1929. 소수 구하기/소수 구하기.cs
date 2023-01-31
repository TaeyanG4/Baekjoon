using System;
using System.Text;

namespace ConsoleApp5
{
    class Program
    {
        static void Main(string[] args)
        {
            StringBuilder st = new StringBuilder();
            string[] arr = Console.ReadLine().Split(" ");
            long M = int.Parse(arr[0]);
            long N = int.Parse(arr[1]);

            bool[] sosu = new bool[N + 1];

            sosu[0] = true;
            sosu[1] = true;

            for (long i = 2; i <= Math.Sqrt(sosu.Length); i++)
            {
                if (sosu[i]) continue;
                for (long j = i * i; j < sosu.Length; j += i)
                {
                    sosu[j] = true;

                }
            }

            for (long i = M; i <= N; i++)
            {
                if (sosu[i] == false) st.Append(i).Append('\n');
            }
            Console.WriteLine(st);
        }
    }
}
