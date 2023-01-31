using System;
using System.Numerics;
namespace ConsoleApp5
{
    class MainApp
    {
        static void Main(string[] args)
        {
            Console.ReadLine();
            BigInteger a = BigInteger.Parse(Console.ReadLine());
            BigInteger b = BigInteger.Parse(Console.ReadLine());
            Console.WriteLine(a * b);

        }
    }
}