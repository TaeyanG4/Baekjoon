using System;
namespace ConsoleApp5
{
    class Program
    {
        static void Main(string[] args)
        {
            int[] a = Array.ConvertAll(Console.ReadLine().Split(), int.Parse);
            int[] b = Array.ConvertAll(Console.ReadLine().Split(), int.Parse);
            foreach (int e in b)
            {
                Console.Write(e - a[0] * a[1] + " ");
            }
        }
    }
}