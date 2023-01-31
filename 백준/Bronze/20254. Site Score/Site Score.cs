using System;

namespace ConsoleApp5
{
    class MainApp
    {
        static void Main(string[] args)
        {
            int[] a = Array.ConvertAll(Console.ReadLine().Split(),int.Parse);
            Console.WriteLine((a[0]*56)+(a[1]*24)+(a[2]*14)+(a[3]*6));
            
        }
    }
}