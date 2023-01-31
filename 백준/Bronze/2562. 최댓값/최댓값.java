import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = 9;
        int[] value = new int[N];
        int num = 1;

        for(int i=0;i<N;i++){
            value[i] = sc.nextInt();
        }

        int temp = value[0];

        for(int i=0;i<N-1;i++){
            for(int j=1;j<N;j++){
                if(temp <= value[j]){
                    temp = value[j];
                    num = j+1;
                }
            }
        }
        System.out.println(temp);
        System.out.println(num);
    }
}
