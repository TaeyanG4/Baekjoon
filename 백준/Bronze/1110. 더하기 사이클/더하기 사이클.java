import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int su = sc.nextInt();

        int a;
        int b;
        int x=su;

        int sum= 0;
        while(true){
            a = su/10;
            b = su%10;

            a = (a + b)%10;
            b = b * 10;

            su = a+b;
            sum++;
            if(x == su) break;
        }
        System.out.println(sum);
    }
}