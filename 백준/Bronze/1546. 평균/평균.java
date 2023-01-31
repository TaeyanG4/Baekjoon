import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int num = sc.nextInt();
        float[] score = new float[num];
        float M=0;
        float su=0;
        for(int i=0;i<num;i++){
            score[i] = sc.nextInt();
            if(score[i] >= M) M = score[i];
        }

        for(int i=0;i<num;i++){
            score[i] = (score[i]/M)*100;
        }

        for(int i=0;i<num;i++){
            su += score[i];
        }
        System.out.println(su/num);
    }
}
