using System;
using System.Numerics;

namespace ConsoleApp5
{
    class MainApp
    {
        static void solveNow()
        {
            String[] str = Console.ReadLine().Split();
            BigInteger a = BigInteger.Parse(str[0]);
            BigInteger b = BigInteger.Parse(str[1]);
            Console.WriteLine(a + b);
        }
        static void Main(string[] args)
        {
            solveNow();
        }
    }
}