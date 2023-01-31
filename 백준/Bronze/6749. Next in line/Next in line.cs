using System;

namespace ConsoleApp5
{
    interface IMyInterface
    {
        int get();
        void set(int inpu1,int inpu2);
        void app1();
    }

    class MyClass :IMyInterface
    {
        private int input1, input2;
        private int result;

        public MyClass() { }
        public MyClass(int input1,int input2)
        {
            this.input1 = input1;
            this.input2 = input2;
        }

        public int get()
        {
            return result;
        }

        public void set(int input1,int input2)
        {
            this.input1 = input1;
            this.input2 = input2;
        }
        public void app1()
        {
            result = input2 + (input2 - input1);
        }

    }

    class MainApp
    {
        static void solveNow()
        {
            try
            {
                int input1 = int.Parse(Console.ReadLine());
                int input2 = int.Parse(Console.ReadLine());

                MyClass myclass = new MyClass();
                myclass.set(input1, input2);
                myclass.app1();
                Console.WriteLine(myclass.get());
            }
            catch(Exception e)
            {
                Console.WriteLine($"에러발생 : {e.Message}");
            }
            
        }

        static void Main(string[] args)
        {
            solveNow();
        }
    }
}