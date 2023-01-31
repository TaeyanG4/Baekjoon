using System;

namespace ConsoleApp5
{
    class MainApp
    {
        static void Main(string[] args)
        {
            int[] a = Array.ConvertAll(Console.ReadLine().Split(), int.Parse);
            int[] c = Array.ConvertAll(Console.ReadLine().Split(), int.Parse);

            Console.WriteLine($"{c[0] - a[2]} {c[1]/a[1]} {c[2] - a[0]}");
        }
    }
}