using System;
using System.Numerics;
using System.Linq.Expressions;
using System.Collections.Generic;
using System.Linq;

namespace ConsoleApp5
{
    
    class MainApp
    {
        static int RunApp(int n1, int n2, int n3)
        {
            if (n1 == n2 && n2 == n3)
            {
                return 10000 + (n1 * 1000);
            }
            else if (n1 == n2 && n1 != n3)
            {
                return 1000 + (n1 * 100);
            }
            else if (n2 == n3 && n2 != n1)
            {
                return 1000 + (n2 * 100);
            }
            else if (n3 == n1 && n3 != n2)
            {
                return 1000 + (n3 * 100);
            }
            else
            {
                if (n1 > n2 && n1 > n3) return 100 * n1;
                if (n2 > n3 && n2 > n1) return 100 * n2;
                if (n3 > n1 && n3 > n2) return 100 * n3;
            }
            return 0;
        }

        static void Main(string[] args)
        {
            int[] n = Array.ConvertAll(Console.ReadLine().Split(), int.Parse);
            Console.WriteLine(RunApp(n[0], n[1], n[2]));
        }
    }
}