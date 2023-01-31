using System;


namespace ConsoleApp5
{
    class Program
    {
        static void Main(string[] args)
        {
            long[] val = Array.ConvertAll(Console.ReadLine().Split(),long.Parse);
            long a, b, v;
            a = val[0];
            b = val[1];
            v = val[2];

            long val2 = (v - b) / (a - b);

            if ((v - b) % (a - b) == 0) Console.WriteLine(val2);
            else Console.WriteLine(val2 + 1);

        }
    }
}