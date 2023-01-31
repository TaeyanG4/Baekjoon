import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        StringBuffer sb = new StringBuffer(sc.next());
        StringBuffer sb2 = new StringBuffer(sc.next());

        sb.reverse();
        sb2.reverse();

        String str = sb.toString();
        String str2 = sb2.toString();

        int a = Integer.parseInt(str);
        int b = Integer.parseInt(str2);

        if(a > b){
            System.out.println(a);
        }
        else{
            System.out.println(b);
        }
    }
}
