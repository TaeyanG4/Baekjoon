import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        int[] arr = new int[26];

        Scanner scan = new Scanner(System.in);
        String key = scan.next();
        for(int i = 0; i < key.length(); i++) {
            char ch = key.charAt(i);
            arr[ch < 97 ? ch - 65 : ch - 97]++;
        }

        int max = 0;
        char maxChar = 0;

        for(int i = 0; i < arr.length; i++) {
            int count = arr[i];
            //System.out.println(count + ", " + max);
            if(count > max) {
                max = count;
                maxChar = (char)(i + 65);
            } else if(count == max) {
                maxChar = '?';
            }
        }

        System.out.println(maxChar);
        // A = 65, a = 97
    }
}