using System;


namespace ConsoleApp4
{

    interface IMyClass
    {
        void setData(int a);
        void outData();
        void app1();
    }

    class MyClass : IMyClass
    {
        public int a;
        public MyClass() { }

        public void setData(int a)
        {
            this.a = a;
        }

        public void outData()
        {
            
        }

        public void app1()
        {
            for (int i = 0; i < a; i++)
            {
                for (int j = 0; j < a-i; j++)
                {
                    Console.Write("*");
                }
                Console.WriteLine();
            }
        }
    }
    

    class MainApp
    {
        static void Main(string[] args)
        {
            MyClass myClass = new MyClass();
            myClass.setData(Convert.ToInt32(Console.ReadLine()));
            myClass.app1();
        }
    }
}