using System;
using System.Numerics;

namespace ConsoleApp5
{
    class MainApp
    {
        static void solveNow()
        {
            ulong[] a = Array.ConvertAll(Console.ReadLine().Split(), ulong.Parse);
            Console.WriteLine(a[0] + a[1] + a[2]);
        }
        static void Main(string[] args)
        {
            solveNow();
        }
    }
}