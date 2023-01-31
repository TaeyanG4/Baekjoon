import java.util.*;
import java.io.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int cost = sc.nextInt();
        int prod = sc.nextInt();
        int price = sc.nextInt();

        int num = 0;
        for (int i = 1;; i++) {
            if(prod >= price) {
                num = -1;
                break;
            }
            num++;
            if(cost < (price - prod) * i) break;
        }
        System.out.println(num);
    }
}
