using System;
using System.Numerics;
namespace ConsoleApp5
{
    class MainApp
    {
        static void Main(string[] args)
        {
            int a = int.Parse(Console.ReadLine());
            int result = a % 5 == 0 ? a / 5 : a / 5 + 1;
            Console.WriteLine(result);
        }
    }
}