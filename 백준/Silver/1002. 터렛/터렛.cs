using System;


namespace ConsoleApp4
{
    struct Circle
    {
        public int x1, y1, r1;
        public int x2, y2, r2;
    }
   
    class MainApp
    {
        static void Main(string[] args)
        {
            int count;
            count = Convert.ToInt32(Console.ReadLine());

            Circle[] arr = new Circle[count];
            

            for (int i = 0; i < count; i++)
            {
                String temp = Console.ReadLine();
                String[] arrs = temp.Split(new String[] { " " }, StringSplitOptions.None);
                arr[i].x1 = Convert.ToInt32(arrs[0]);
                arr[i].y1 = Convert.ToInt32(arrs[1]);
                arr[i].r1 = Convert.ToInt32(arrs[2]);
                arr[i].x2 = Convert.ToInt32(arrs[3]);
                arr[i].y2 = Convert.ToInt32(arrs[4]);
                arr[i].r2 = Convert.ToInt32(arrs[5]);
            }

            for (int i = 0; i < count; i++)
            {
                if (arr[i].x1==arr[i].x2&&arr[i].y1==arr[i].y2&&arr[i].r1==arr[i].r2)
                    Console.WriteLine("-1");
                else if (Math.Pow(arr[i].x1 - arr[i].x2, 2) + Math.Pow(arr[i].y1 - arr[i].y2, 2) > Math.Pow(arr[i].r1 + arr[i].r2, 2) || Math.Pow(arr[i].x1 - arr[i].x2, 2) + Math.Pow(arr[i].y1 - arr[i].y2, 2) < Math.Pow(arr[i].r1 - arr[i].r2,2))
                    Console.WriteLine("0");
                else if (Math.Pow(arr[i].x1 - arr[i].x2, 2) + Math.Pow(arr[i].y1 - arr[i].y2, 2) == Math.Pow(arr[i].r1 + arr[i].r2, 2) || Math.Pow(arr[i].x1 - arr[i].x2, 2) + Math.Pow(arr[i].y1 - arr[i].y2, 2) == Math.Pow(arr[i].r1 - arr[i].r2, 2))
                    Console.WriteLine("1");
                else
                    Console.WriteLine("2");
            }

        }
    }


}