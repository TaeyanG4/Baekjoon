using System;


namespace ConsoleApp4
{

    interface IMyClass
    {
        void setData(int count);
        void outData();
        void app1();
    }

    struct Point
    {
        public int x1, y1;
    }

    class MyClass : IMyClass
    {
        public int count;
        public int value = 0;
        public Point[] inputData;
        public int[,] area = new int[101,101];

        public MyClass() { }

        public void setData(int count)
        {
            this.count = count;
            inputData = new Point[count];

            for (int i = 0; i < count; i++)
            {
                string[] stringArr = Console.ReadLine().Split(new string[] {" "}, StringSplitOptions.None);
                inputData[i].x1 = Convert.ToInt32(stringArr[0]);
                inputData[i].y1 = Convert.ToInt32(stringArr[1]);
            }

            try
            {
                for (int i = 0; i < 101; i++)
                {
                    for (int j = 0; j < 101; j++)
                    {
                        area[i, j] = 0;
                    }
                }
            }
            catch (System.IndexOutOfRangeException)
            {
                Console.WriteLine("error");
            }
            
        }

        public void outData()
        {
                Console.WriteLine($"{value}");
        }

        public void app1()
        {
            int x, y;

            try
            {
                for (int i = 0; i < count; i++)
                {
                    for (int j = 0; j < 10; j++)
                    {
                        for (int k = 0; k < 10; k++)
                        {
                            if (j + inputData[i].x1 <= 0 && j + inputData[i].x1 >= 100) break;
                            if (k + inputData[i].y1 <= 0 && k + inputData[i].y1 >= 100) break;
                            x = j + inputData[i].x1;
                            y = k + inputData[i].y1;
                            area[x, y] = 1;
                        }
                    }
                }
            }
            catch(System.IndexOutOfRangeException)
            {
                Console.WriteLine("error");
            }

            try
            {

                for (int i = 0; i < 101; i++)
                {
                    for (int j = 0; j < 101; j++)
                    {
                        if (area[i, j] == 1)
                        {
                            value++;
                        }
                    }
                }
                
            }
            catch (System.IndexOutOfRangeException)
            {
                Console.WriteLine("error");
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
            myClass.outData();
        }
    }
}