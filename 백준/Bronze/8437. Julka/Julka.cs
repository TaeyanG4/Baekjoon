using System;
using System.Numerics;

namespace ConsoleApp5
{
    class MainApp
    {
        static void solveNow()
        {
                //int[] inputdata = Array.ConvertAll(Console.ReadLine().Split(), int.Parse);
            BigInteger a = BigInteger.Parse(Console.ReadLine());
            BigInteger b = BigInteger.Parse(Console.ReadLine());

            if (a % 2 == 0)
            {
                Console.WriteLine((a / 2) + (b / 2));
                Console.WriteLine((a / 2) - (b / 2));
            }
            else
            {
                Console.WriteLine((a / 2) + (b / 2)+1);
                Console.WriteLine((a / 2) - (b / 2));
            }
        }

        static void Main(string[] args)
        {
            solveNow();
        }
    }
}