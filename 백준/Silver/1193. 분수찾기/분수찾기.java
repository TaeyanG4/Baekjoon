import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int value = sc.nextInt();

        int set = 1;
        int num = 0;

        int a = 0,b = 0;

        for (int i = 0; i < value; i++) {
            if(set==num){
                set++;
                num=1;
            }
            else{
                num++;
            }

            if(set % 2 == 0){
                a = num;
                b = (set-num)+1;
            }
            else{
                a = (set-num)+1;
                b = num;
            }
        }
        System.out.println(a+"/"+b);
    }
}

