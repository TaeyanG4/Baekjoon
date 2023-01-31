using System;

namespace ConsoleApp5
{
    class Program
    {
        static void Main(string[] args)
        {
            int[] a = Array.ConvertAll(Console.ReadLine().Split(), int.Parse);
            int[] b = new int[] { 1, 1, 2, 2, 2, 8 };
            for (int i = 0; i < a.Length; i++)
            {
                Console.Write("{0} ", b[i] - a[i]);
            }
        }
    }
}