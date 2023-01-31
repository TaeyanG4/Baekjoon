using System;
using System.Numerics;
using System.Linq.Expressions;
using System.Collections.Generic;

namespace ConsoleApp5
{
    class MyClass
    {
        char[,] wb = new char[8, 8];
        char[,] bw = new char[8, 8];
        char[,] p_board;

        public void MakeBoard(int H,int W)
        {
            p_board = new char[H, W];
            char[] c;
            for (int i = 0; i < H; i++)
            {
                c = Console.ReadLine().ToCharArray();
                for (int j = 0; j < W; j++)
                {
                    p_board[i, j] = c[j];
                }
            }
        }

        public void BaseBoard()
        {
            for (int i = 0; i < wb.GetLength(0); i++)
            {
                for (int j = 0; j < wb.GetLength(1); j++)
                {
                    wb[i, j] = ((i + j) % 2) == 0 ? 'W' : 'B';
                }
            }

            for (int i = 0; i < bw.GetLength(0); i++)
            {
                for (int j = 0; j < bw.GetLength(1); j++)
                {
                    bw[i, j] = ((i + j) % 2) == 0 ? 'B' : 'W';
                }
            }
        }

        public int CheckBoardW(int a, int b)
        {
            int count = 0;

            for (int i = 0; i < wb.GetLength(0); i++) 
            {
                for (int j = 0; j < wb.GetLength(1); j++) 
                {
                    if (wb[i, j] != p_board[i + a, j + b]) count++;
                }
            }
            return count;
        }

        public int CheckBoardB(int a, int b)
        {
            int count = 0;

            for (int i = 0; i < bw.GetLength(0); i++)
            {
                for (int j = 0; j < bw.GetLength(1); j++)
                {
                    if (bw[i, j] != p_board[i + a, j + b]) count++;
                }
            }
            return count;
        }
    }

    class MainApp
    {
        static public int runApp()
        {
            MyClass myClass = new MyClass();

            int[] input = Array.ConvertAll(Console.ReadLine().Split(), int.Parse);
            int h = input[0];
            int w = input[1];

            myClass.MakeBoard(h, w);
            myClass.BaseBoard();

            int result = 5000;
            int val = 0;

            for (int i = 0; i < h - 7; i++) 
            {
                for (int j = 0; j < w - 7; j++) 
                {
                    val = myClass.CheckBoardW(i, j);
                    if (result > val) 
                    {
                        result = val;
                    }
                }
            }

            for (int i = 0; i < h - 7; i++)
            {
                for (int j = 0; j < w - 7; j++)
                {
                    val = myClass.CheckBoardB(i, j);
                    if (result > val)
                    {
                        result = val;
                    }
                }
            }

            return result;
        }

        static void Main(string[] args)
        {
            Console.WriteLine(runApp());
        }
    }
}