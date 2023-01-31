using System;

namespace ConsoleApp5
{
    class MainApp
    {
        static void Main(string[] args)
        {
            int[] a = Array.ConvertAll(Console.ReadLine().Split(), int.Parse);
            Console.WriteLine($"{a[1] - a[0]} {a[1]}");
        }
    }
}