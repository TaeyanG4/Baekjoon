import java.util.*;
public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int temp;
        int min = 1000000,max = -1000000;

        for(int i=0;i<N;i++){
            temp = sc.nextInt();
            if(temp <= min) min = temp;
            if(temp >= max) max = temp;
        }

        System.out.println(min+" "+max);
    }
}