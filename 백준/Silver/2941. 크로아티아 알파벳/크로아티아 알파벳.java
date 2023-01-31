import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String input = sc.next();
        int count = 0;

        for (int i = 0; i < input.length(); i++) {
            if(input.charAt(i) == 'c'){
                if(i == input.length()-1) break;
                if(input.charAt(i+1) == '-' || input.charAt(i+1) == '=') {
                    i++;
                    count++;
                }
            }
            if(input.charAt(i) == 'd'){
                if(i == input.length()-1) break;
                if(input.charAt(i+1) == '-') {
                    i++;
                    count++;
                }
            }
            if(input.charAt(i) == 'd'){
                if(i == input.length()-2) break;
                if(input.charAt(i+1) == 'z') {
                    if(input.charAt(i+2) == '=') {
                        i+=2;
                        count+=2;
                    }
                }
            }
            if(input.charAt(i) == 'l'){
                if(i == input.length()-1) break;
                if(input.charAt(i+1) == 'j') {
                    i++;
                    count++;
                }
            }
            if(input.charAt(i) == 'n'){
                if(i == input.length()-1) break;
                if(input.charAt(i+1) == 'j') {
                    i++;
                    count++;
                }
            }
            if(input.charAt(i) == 's'){
                if(i == input.length()-1) break;
                if(input.charAt(i+1) == '=') {
                    i++;
                    count++;
                }
            }
            if(input.charAt(i) == 'z'){
                if(i == input.length()-1) break;
                if(input.charAt(i+1) == '=') {
                    i++;
                    count++;
                }
            }
        }

        System.out.println(input.length()-count);
    }
}
