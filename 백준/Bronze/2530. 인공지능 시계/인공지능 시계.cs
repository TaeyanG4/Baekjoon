using System;
using System.Numerics;
using System.Linq.Expressions;
using System.Collections.Generic;
using System.Linq;

namespace ConsoleApp5 
{ 
    class MainApp
    {
        static void RunApp(int[] t, int n)
        {
            var a = new TimeSpan(t[0], t[1], t[2]);
            var b = new TimeSpan(0, 0, n);
            var result = a + b;
            Console.WriteLine($"{result.Hours} {result.Minutes} {result.Seconds}");
        }

        static void Main(string[] args)
        {
            int[] t = Array.ConvertAll(Console.ReadLine().Split(), int.Parse);
            int n = int.Parse(Console.ReadLine());

            RunApp(t, n);
        }
    }
}