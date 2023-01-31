using System;

namespace ConsoleApp5
{
    class MainApp
    {
        static void Main(string[] args)
        {
            Console.WriteLine(DateTime.UtcNow.ToString("yyyy"));
            Console.WriteLine(DateTime.UtcNow.ToString("MM"));
            Console.WriteLine(DateTime.UtcNow.ToString("dd"));
        }
    }
}