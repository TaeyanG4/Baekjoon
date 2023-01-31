import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] arr = new int[10];

        for(int i=0;i<10;i++){
            arr[i] = sc.nextInt()%42;
        }
        int num=0;

        for(int i=0;i<42;i++){
            for(int j=0;j<10;j++){
                if(arr[j] == i) {
                    num++;
                    break;
                }
            }
        }
        System.out.println(num);
    }
}
