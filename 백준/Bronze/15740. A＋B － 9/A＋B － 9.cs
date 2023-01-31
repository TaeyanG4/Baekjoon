using System;
using System.Numerics;
namespace ConsoleApp5
{
    class MainApp
    {
        static void Main(string[] args)
        {
            String[] input = Console.ReadLine().Split();
            BigInteger a = BigInteger.Parse(input[0]);
            BigInteger b = BigInteger.Parse(input[1]);
            Console.WriteLine(a + b);
        }
    }
}