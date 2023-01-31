import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String userInput = sc.next();
        int outputData = 0;
        for (int i = 0; i < userInput.length(); i++) {

            if (userInput.charAt(i) <= 'C') {
                outputData += 3; //ABC
            } else if (userInput.charAt(i) >= 'D' && userInput.charAt(i) <= 'F') {
                outputData += 4; //DEF
            } else if (userInput.charAt(i) >= 'G' && userInput.charAt(i) <= 'I') {
                outputData += 5; //GHI
            } else if (userInput.charAt(i) >= 'J' && userInput.charAt(i) <= 'L') {
                outputData += 6; //JKL
            } else if (userInput.charAt(i) >= 'M' && userInput.charAt(i) <= 'O') {
                outputData += 7; //MNO
            } else if (userInput.charAt(i) >= 'P' && userInput.charAt(i) <= 'S') {
                outputData += 8; //PQRS
            } else if (userInput.charAt(i) >= 'T' && userInput.charAt(i) <= 'V') {
                outputData += 9; //TUV
            } else if (userInput.charAt(i) >= 'W' && userInput.charAt(i) <= 'Z') {
                outputData += 10; //WXYZ
            }
        }
        System.out.println(outputData);
    }
}
