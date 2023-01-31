import java.util.Scanner;
public class Main {
    static boolean function (int a) {
        int temp,temp2;
        temp = ((a / 10) % 10)-(a % 10);
        a = a / 10;
        temp2 = ((a / 10) % 10)-(a % 10);
        if(a/10 == 0) return true;
        else if(temp != temp2) return false;
        else return function(a);
    }
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int userInput = sc.nextInt();
        int sum = 0;
        for (int i = 1; i <= userInput; i++) if(function(i)) sum++;
        System.out.println(sum);
    }
}