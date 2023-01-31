import java.util.Scanner;

public class Main {
    public static void main(String [] agrs){
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();

        int div = a/b;
        int quo = a%b;

        System.out.print(div);

        if(a/b == 0 || a%b != 0) {
            System.out.print("."+(quo*10)/b);
            if(quo%b != 0){
                int temp = (a*10)%b;

                for(int i=1;i<30;i++){
                    System.out.print(temp*10/b);
                    temp = (temp*10)%b;
                }
            }
        }
    }
}
