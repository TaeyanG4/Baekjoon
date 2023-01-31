using System;
using System.Numerics;
using System.Linq.Expressions;
using System.Collections.Generic;
using System.Linq;

namespace ConsoleApp5 
{ 
    class MainApp
    {
        static int RunApp(int n)
        {
            int result;
            if (n % 2 == 0)
            {
                result = (n / 2 + 1) * (n / 2 + 1);
            }
            else
            {
                result = (n / 2 + 1) * (n / 2 + 2);
            }

            return result;
        }

        static void Main(string[] args)
        {
            //int[] t = Array.ConvertAll(Console.ReadLine().Split(), int.Parse);
            int n = int.Parse(Console.ReadLine());
            Console.WriteLine(RunApp(n));
        }
    }
}