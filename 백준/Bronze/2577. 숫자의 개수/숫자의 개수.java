import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int temp = 1;

        for(int i=0;i<3;i++){
            temp *= sc.nextInt();
        }

        int[] arr = new int[10];
        int sum = 0;
        for(int i=0;i<arr.length;i++){
            if((int)Math.pow(10,i) - temp >0) break;
            sum++;
        }
        for(int i = 0 ;i < sum ;i++){
            arr[i] = temp%(int)Math.pow(10,i+1)-temp%(int)Math.pow(10,i);
            arr[i] = arr[i]/(int)Math.pow(10,i);
        }

        int[] arrValue = {0,0,0,0,0,0,0,0,0,0};

        for(int i=0;i<sum;i++){
            for(int j=0;j<arrValue.length;j++){
                if(arr[i] == j){
                    arrValue[j]++;
                    break;
                }
            }
        }

        for(int k : arrValue){
            System.out.println(k);
        }
    }
}
