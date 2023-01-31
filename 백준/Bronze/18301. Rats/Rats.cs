using System;

namespace ConsoleApp5
{
    class MainApp
    {
        static void Main(string[] args)
        {
            int[] a = Array.ConvertAll(Console.ReadLine().Split(),int.Parse);
            Console.WriteLine((a[0]+1)*(a[1]+1)/(a[2]+1)-1);
            
        }
    }
}