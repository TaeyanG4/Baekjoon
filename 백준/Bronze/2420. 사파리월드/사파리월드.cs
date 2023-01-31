using System;
using System.Numerics;
using System.Linq.Expressions;
using System.Collections.Generic;

namespace ConsoleApp5
{
    class MainApp
    {
        static void Main(string[] args)
        {
            long[] input = Array.ConvertAll(Console.ReadLine().Split(), long.Parse);
            Console.WriteLine(Math.Abs(input[0] - input[1]));
        }
    }
}