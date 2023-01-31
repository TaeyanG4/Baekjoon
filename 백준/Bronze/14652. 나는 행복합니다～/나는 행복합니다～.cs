using System;
using System.Numerics;

namespace ConsoleApp5
{
    class MainApp
    {
        static void solveNow()
        {
            int[] input = Array.ConvertAll(Console.ReadLine().Split(), int.Parse);
            int count = 0;

            for (int i = 0; i < input[0]; i++)
            {
                for (int j = 0; j < input[1]; j++)
                {
                    if (count == input[2])
                    {
                        Console.WriteLine(i + " " + j);
                        return;
                    }
                    else count++;
                }
            }
        }
        static void Main(string[] args)
        {
            solveNow();
        }
    }
}