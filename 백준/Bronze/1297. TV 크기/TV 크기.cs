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
            double[] input = Array.ConvertAll(Console.ReadLine().Split(), double.Parse);
            Func<double, double, double, double> func1 = (d, h, w) =>
            {
                double x = Math.Pow(d, 2) / (Math.Pow(h, 2) + Math.Pow(w, 2));
                return Math.Sqrt(x);
            };
            double val = func1(input[0], input[1], input[2]);
            int a = (int)(val * input[1]);
            int b = (int)(val * input[2]);

            Console.WriteLine($"{a} {b}");
        }
    }
}