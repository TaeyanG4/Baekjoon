import java.io.*;
import java.util.*;

public class Main {
    static int sum = 1;
    static int fac(int x){
        sum *= x;
        if(x == 1) return sum;
        else {
            x--;
            return fac(x);
        }
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int num = sc.nextInt();
        if(num == 0){
            System.out.println(1);
        }
        else{
            System.out.println(fac(num));
        }
    }
}
