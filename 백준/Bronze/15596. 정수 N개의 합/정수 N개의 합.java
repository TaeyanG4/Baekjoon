import java.util.Scanner;

public class Test {
    static long sum(int[] a) {
        long ans = 0;
        for (int i = 0; i < a.length; i++) {
            ans += a[i];
        }
        return ans;
    }
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int su = sc.nextInt();
        int[] arr = new int[su];

        System.out.println(sum(arr));
    }
}
