using System;


namespace ConsoleApp4
{

    interface IMyClass
    {
        void setData(int N,int K);
        void outData();
        void App1();
    }

    class MyClass : IMyClass
    {
        private int N = 0, K = 0;
        private int count = 0;
        private int[] valueArr;
        private int[] outputArr;

        public MyClass() { }
        public MyClass(int N,int K)
        {
            this.N = N;
            this.K = K; 
        }

        public void setData(int N,int K)
        {
            this.N = N;
            this.K = K;
        }

        public void outData()
        {
            Console.Write("<");
            for (int i = 0; i < outputArr.Length; i++)
            {
                Console.Write($"{outputArr[i]}");
                if (i + 1 == outputArr.Length) break;
                Console.Write(", ");
            }
            Console.Write(">");
        }

        public void App1()
        {
            int Kcount = 0;
            valueArr = new int[N];
            outputArr = new int[N];

            for (int i = 0; i < valueArr.Length; i++)
            {
                valueArr[i] = i+1;
            }

            for (int i = 0; i < outputArr.Length; i++)
            {
                outputArr[i] = 5001;
            }

            while (count != N)
            {
                for (int i = 0; i < N; i++)
                {
                    if (valueArr[i] == 0) continue;

                    Kcount++;

                    if(Kcount == K)
                    {
                        outputArr[count] = valueArr[i];
                        valueArr[i] = 0;
                        count++;
                        Kcount = 0;
                    }
                }
            }
        }
    }
    

    class MainApp
    {
        static void Main(string[] args)
        {

            string[] valueArr = Console.ReadLine().Split(new string[] { }, StringSplitOptions.None);
            int valueN = Convert.ToInt32(valueArr[0]);
            int valueK = Convert.ToInt32(valueArr[1]);

            MyClass myClass = new MyClass();
            myClass.setData(valueN, valueK);
            myClass.App1();
            myClass.outData();
        }
    }

}