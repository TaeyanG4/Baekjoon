using System;
using System.Numerics;
namespace ConsoleApp5
{
    class MainApp
    {
        static void Main(string[] args)
        {
            char[] input = Console.ReadLine().ToCharArray();
            int a = 0;
            for (int i = 0; i < input.Length; i++)
            {
                a = (a * 10+(input[i] - '0')) % 20000303;
            }
            Console.WriteLine(a);
        }
    }
}