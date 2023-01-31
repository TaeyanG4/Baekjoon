using System;

namespace ConsoleApp5
{
    class Program
    {
        static void Main(string[] args)
        {
            string a = Console.ReadLine();
            char[] b = a.ToCharArray();

            int temp;
            int val = 0;
            for (int i = 0; i < b.Length; i++)
            {
                temp = b[^(1+i)] switch
                {
                    '0' => 0,
                    '1' => 1,
                    '2' => 2,
                    '3' => 3,
                    '4' => 4,
                    '5' => 5,
                    '6' => 6,
                    '7' => 7,
                    '8' => 8,
                    '9' => 9,
                    'A' => 10,
                    'B' => 11,
                    'C' => 12,
                    'D' => 13,
                    'E' => 14,
                    'F' => 15,
                     _ => 0
                };
                val += ((int)Math.Pow(16, i) * temp);
            }

            Console.WriteLine(val);
        }
    }
}
