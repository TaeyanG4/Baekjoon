using System;

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
        int[] data;

        public void set(int[] data)
        {
            this.data = data;
        }

        public int get()
        {
            int sum = 0;

            foreach (int d in data)
            {
                sum += (int)Math.Pow(d,2);
            }

            return sum % 10;
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
            string[] sArr = Console.ReadLine().Split(" ");
            int[] iArr = new int[sArr.Length];

            for (int i = 0; i < sArr.Length; i++)
            {
                iArr[i] = int.Parse(sArr[i]);
            }

            myClass.set(iArr);
            Console.WriteLine(myClass.get());
            

        }
    }
}
