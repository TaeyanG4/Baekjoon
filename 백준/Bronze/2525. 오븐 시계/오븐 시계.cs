using System;
using System.Numerics;
using System.Linq.Expressions;
using System.Collections.Generic;
using System.Linq;

namespace ConsoleApp5
{
    
    class MainApp
    {
        static int H,M;
        static void RunApp(int[] t, int n)
        {
            H = t[0];
            M = t[1];

            H += n / 60;
            M += n % 60;

            if (M >= 60)
            {
                M -= 60;
                H++;
            }

            if (H >= 24)
            {
                H -= 24;
            }
        }

        static void Main(string[] args)
        {
            int[] t = Array.ConvertAll(Console.ReadLine().Split(), int.Parse);
            int n = int.Parse(Console.ReadLine());

            RunApp(t, n);
            Console.WriteLine($"{H} {M}");
        }
    }
}