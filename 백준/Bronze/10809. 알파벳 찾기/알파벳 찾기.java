import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {

        LinkedList<Integer> alpha = new LinkedList<>();
        Scanner sc = new Scanner(System.in);

        for (int i = 0; i < 26; i++) {
            alpha.add(-1);
        }

        String userInput = sc.next();
        char[] ch = userInput.toCharArray();


        for (int i = 0; i < userInput.length(); i++) {
            for (int j = 0; j < alpha.size(); j++) {
                if(ch[i] == (j+97) && alpha.get(j) == -1){
                    alpha.remove(j);
                    alpha.add(j,i);
                }
            }
        }

        for (int i = 0; i < alpha.size(); i++) {
            System.out.print(alpha.get(i)+" ");
        }
    }
}
