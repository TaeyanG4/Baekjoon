using System;

namespace ConsoleApp5
{
    class MainApp
    {
        static void Main(string[] args)
        {
            long[] input = Array.ConvertAll(Console.ReadLine().Split(), long.Parse);
            Console.WriteLine((input[0] + input[1]) * (input[0] - input[1]));
        }
    }
}