import java.util.Scanner;

public class Main {

    static int sum;
    static void test(int a,int[] arr){
        sum = 0;
        sum += a;
        while(a>0){
            sum += a%10;
            a /= 10;
        }
        if(sum>10000) return;
        arr[sum] = 0;
        test(sum,arr);
    }

    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        int[] arr = new int[10001];
        for (int i = 1; i < arr.length; i++) {
            arr[i] = i;
        }


        for (int i = 1; i < arr.length; i++) {
            if(arr[i] == 0) continue;
            test(arr[i],arr);
        }

        for (int i = 1; i < arr.length; i++) {
            if(arr[i] != 0){
                System.out.println(arr[i]);
            }
        }

    }
}
