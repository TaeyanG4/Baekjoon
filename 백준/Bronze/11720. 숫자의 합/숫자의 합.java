import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int userInput = sc.nextInt();
        String value = sc.next();
        char[] ch = value.toCharArray();
        int output = 0;
        for (int i = 0; i < userInput; i++) {
            output += ch[i] - 48;
        }
        System.out.println(output);
    }
}
