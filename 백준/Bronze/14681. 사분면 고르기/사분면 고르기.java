import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int value_x = sc.nextInt();
        int value_y = sc.nextInt();

        if(value_x > 0 && value_y > 0){
            System.out.println("1");
        }
        else if(value_x < 0 && value_y > 0){
            System.out.println("2");
        }
        else if(value_x < 0 && value_y < 0){
            System.out.println("3");
        }
        else System.out.println("4");
    }
}
