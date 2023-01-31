using System;

namespace ConsoleApp5
{
    class MainApp
    {
        static void Main(string[] args)
        {
            int a = int.Parse(Console.ReadLine());
            int val1 = a - ((a / 100) * 22);
            int val2 = a - ((a / 100 * 20) / 100 * 22);
            Console.WriteLine($"{val1} {val2}");
            
        }
    }
}