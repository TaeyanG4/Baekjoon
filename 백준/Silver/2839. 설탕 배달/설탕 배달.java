import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int value = sc.nextInt();
        int x = 0;
        while(true){
            if(value % 5 == 0){
                System.out.println((value/5) + x);
                break;
            }
            value = value-3;
            x++;
            if(value < 0) {
                value = -1;
                System.out.println(value);
                break;
            }
        }
    }
}