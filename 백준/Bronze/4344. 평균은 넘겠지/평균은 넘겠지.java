import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int num = sc.nextInt();
        int su1;
        float temp,dap;
        float[] score;
        for (int i = 0; i < num; i++) {
            su1 = sc.nextInt();
            score = new float[su1];
            dap = 0;
            temp = 0;

            for(int j = 0; j < score.length; j++) {
                score[j] = sc.nextFloat();
                dap += score[j];
                temp = dap/su1;
            }

            int su2 = 0;
            for (float v : score) {
                if (v > temp) {
                    su2++;
                }
            }

            dap = (float)su2 / (float)su1;
            System.out.println(String.format("%.3f",(dap*100))+"%");
        }
    }
}
