using System;
using System.IO;


namespace ConsoleApp4
{

    interface ISumtest
    {
        int A
        {
            set;
            get;
        }

        int B
        {
            set;
            get;
        }

        int Sum();
    }

    abstract class abSumtest : ISumtest
    {
        abstract public int A
        {
            set;
            get;
        }

        abstract public int B
        {
            set;
            get;
        }

        abstract public int Sum();
    }

    class Sumtest : abSumtest
    {
        public override int A
        {
            set;
            get;
        }

        public override int B
        {
            set;
            get;
        }

        public override int Sum()
        {
            return A + B;
        }
    }
    

    class MainApp
    {
        static void Main(string[] args)
        {
            Sumtest sum1 = new Sumtest();
            sum1.A = Convert.ToInt32(Console.ReadLine());
            sum1.B = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine(sum1.Sum());
        }
    }

}