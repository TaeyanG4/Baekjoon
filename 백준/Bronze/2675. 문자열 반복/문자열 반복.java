import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int userInputNum = sc.nextInt();
        int userInputR = 0;
        String userInputS = "";
        String outputData = "";
        for (int i = 0; i < userInputNum; i++) {

            userInputR = sc.nextInt();
            userInputS = sc.next();

            char [] ch = userInputS.toCharArray();
            for (char c : ch) {
                for (int k = 0; k < userInputR; k++) {
                    outputData += c;
                }
            }

            System.out.println(outputData);
            outputData = "";
        }
    }
}
