using System;
using System.Numerics;

namespace ConsoleApp5
{
    interface IMyinterface
    {
        void set();
        int get();
        void app1();
    }

    class MyClass
    {


        public void set(int[] input_data)
        {
        }

        public int get()
        {
            return 0;
        }

        public void app1()
        {


        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            MyClass myClass = new MyClass();
            string[] arr = Console.ReadLine().Split();
            BigInteger bigint1 = BigInteger.Parse(arr[0]);
            BigInteger bigint2 = BigInteger.Parse(arr[1]);
            BigInteger output1;
            BigInteger output2 = BigInteger.DivRem(bigint1, bigint2,out output1);
            Console.WriteLine(output2);
            Console.WriteLine(output1);

        }
    }
}
