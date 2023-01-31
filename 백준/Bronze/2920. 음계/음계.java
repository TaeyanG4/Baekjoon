import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = 8;
        String value = "";

        String ascending = "12345678";
        String descending = "87654321";

        for(int i=0;i<N;i++){
            value += sc.nextInt();
        }

        if(ascending.equals(value)) {
            System.out.println("ascending");
        }
        else if(descending.equals(value)) {
            System.out.println("descending");
        }
        else System.out.println("mixed");
    }
}
