using System;

namespace ConsoleApp5
{
    class MyClass
    {
        
    }

    class Program
    {
        public static bool[] sosu;

        static void Main(string[] args)
        {
            int N = int.Parse(Console.ReadLine());
            app(N);
        }

        public static void app(int N)
        {

            bool[] sosu = new bool[N+1];
            sosu[0] = sosu[1] = true;

            for (int i = 2; i <= Math.Sqrt(sosu.Length); i++)
            {
                if (sosu[i]) continue;
                for (int j = i*i; j < sosu.Length; j = j+i)
                {
                    sosu[j] = true;
                }
            }

            int temp = N;
            for (int i = 2; i < sosu.Length; i++)
            {
                if (sosu[i]) continue;
                for (int j = 0; j < sosu.Length; j++)
                {
                    if (temp % i == 0)
                    {
                        Console.WriteLine(i);
                        temp = temp / i;
                    }
                    else break;
                }
            }
        }
    }
}
