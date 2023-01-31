using System;
using static System.Console;

namespace ConsoleApp3
{
    class Program
    {

        static void Main(string[] args)
        {
            int count = 0;
            String n = Console.ReadLine();
            String[] input = new String[int.Parse(n)];

            for (int i = 0; i < input.Length; i++)
            {
                input[i] = Console.ReadLine();
            }

            int[] alpha = new int[150];

            for (int k = 0; k < input.Length; k++)
            {

                for (int i = 0; i < 150; i++)
                {
                    alpha[i] = 0;
                }

                Char[] arr = new char[input[k].Length];
                arr = input[k].ToCharArray();
                Char? temp = null;
                for (int j = 0; j <= arr.Length; j++) //단어 검사
                {
                    if (j == (arr.Length))
                    {
                        count++;
                        break;
                    }

                    if (temp == arr[j]) 
                    { 
                        continue; 
                    }
                    else 
                    {
                        temp = arr[j];
                        alpha[arr[j]]++;
                        //Console.WriteLine($"{temp}");
                        //Console.WriteLine($"{arr[j]}");
                        //Console.WriteLine($"{alpha[arr[j]]}");
                    }

                    if (alpha[arr[j]] == 2) break;
                }
            }
            Console.WriteLine(count);
            
        }
    }
}