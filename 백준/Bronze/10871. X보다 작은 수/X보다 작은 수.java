import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int x = sc.nextInt();

        int[] su = new int[n];
        for(int i=0;i<n;i++){
            su[i] = sc.nextInt();
        }

        for(int i=0;i<n;i++){
            if(su[i] < x) System.out.print(su[i]+" ");
        }
    }
}