using System;
using System.Numerics;
using System.Linq.Expressions;
using System.Collections.Generic;
using System.Linq;

namespace ConsoleApp5 
{ 
    class MainApp
    {
        static void RunApp(int[] t)
        {
            var a = from c in t
                    orderby c
                    select c;

            foreach (var c in a)
            {
                Console.Write($"{c} ");
            }
        }

        static void Main(string[] args)
        {
            int[] t = Array.ConvertAll(Console.ReadLine().Split(), int.Parse);

            RunApp(t);
        }
    }
}