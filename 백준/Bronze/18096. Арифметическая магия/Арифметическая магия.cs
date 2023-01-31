using System;

namespace ConsoleApp5
{
    class MainApp
    {
        static void Main(string[] args)
        {
            int[] a = Array.ConvertAll(Console.ReadLine().Split(), int.Parse);
            int x = 2;
            int y = 2;
            int n = a[0];
            int val = (int)Math.Pow(((x + 1) * (y + 1) - x * y - x - y), n);
            Console.WriteLine(val);
        }
    }
}