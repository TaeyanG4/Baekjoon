using System;

namespace ConsoleApp5
{
    class Program
    {
        static void Main(string[] args)
        {
            int a = 0;
            for (int i = 0; i < 4; i++)
            {
                a += int.Parse(Console.ReadLine());
            }
            int val1;
            int val2 = Math.DivRem(a, 60, out val1);
            Console.WriteLine(val2);
            Console.WriteLine(val1);
        }
    }
}