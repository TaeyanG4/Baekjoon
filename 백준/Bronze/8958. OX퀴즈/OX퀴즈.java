import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int num = sc.nextInt();
        String[] dap = new String[num];

        for(int i=0;i<num;i++){
            dap[i] = sc.next();
        }

        int sum = 1;
        int temp = 0;

        for(int i=0;i<num;i++){
            for(int j=0;j<dap[i].length();j++){
                if(dap[i].charAt(j) == 'O'){
                    temp += sum;
                    sum++;
                }
                else sum = 1;
            }
            System.out.println(temp);
            temp = 0;
            sum = 1;
        }
    }
}
