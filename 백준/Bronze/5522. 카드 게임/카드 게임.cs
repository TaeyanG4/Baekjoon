using System;

namespace ConsoleApp5
{
    class Program
    {
        static void Main(string[] args)
        {
            int a = 0;
            for (int i = 0; i < 5; i++)
            {
                a += int.Parse(Console.ReadLine());
            }
            Console.WriteLine(a);
        }
    }
}