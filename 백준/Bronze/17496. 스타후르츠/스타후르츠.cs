using System;

namespace ConsoleApp5
{
    class MainApp
    {
        static void Main(string[] args)
        {
            String[] input = Console.ReadLine().Split();
            int N = int.Parse(input[0]);
            int T = int.Parse(input[1]);
            int C = int.Parse(input[2]);
            int P = int.Parse(input[3]);

            Console.WriteLine((N - 1) / T * C * P);
        }
    }
}