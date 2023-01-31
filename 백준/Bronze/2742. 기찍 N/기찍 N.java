import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        System.out.println(n);
        for(int i=n;n>1;i--){
            System.out.println(n -= 1);
        }
    }
}