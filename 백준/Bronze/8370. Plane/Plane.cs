using System;

namespace ConsoleApp5
{
    interface IMyInterface
    {
        int get();
        void set(int input1);
        void app1();
    }

    class MyClass : IMyInterface
    {
        private int input1, input2, input3, input4;
        private int result;

        //Constuct
        public MyClass() { }

        public MyClass(int input1)
        {
            this.input1 = input1;
        }

        public MyClass(int input1, int input2) : this(input1)
        {
            this.input2 = input2;
        }

        public MyClass(int input1, int input2, int input3) : this(input1, input2)
        {
            this.input3 = input3;
        }

        public MyClass(int input1, int input2, int input3, int input4) : this(input1, input2, input3)
        {
            this.input4 = input4;
        }

        //get
        public int get()
        {
            return result;
        }

        //set
        public void set(int input1)
        {
            this.input1 = input1;
        }

        public void set(int input1, int input2)
        {
            this.input1 = input1;
            this.input2 = input2;
        }

        public void set(int input1, int input2, int input3)
        {
            this.input1 = input1;
            this.input2 = input2;
            this.input3 = input3;
        }

        public void set(int input1, int input2, int input3, int input4)
        {
            this.input1 = input1;
            this.input2 = input2;
            this.input3 = input3;
            this.input4 = input4;
        }
        
        //app
        public void app1()
        {
            result = input1 * input2 + input3 * input4;
        }

    }

    class MainApp
    {
        static void solveNow()
        {
            try
            {
                int[] inputdata = Array.ConvertAll(Console.ReadLine().Split(), int.Parse);

                MyClass myclass = new MyClass();
                myclass.set(inputdata[0], inputdata[1], inputdata[2], inputdata[3]);
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