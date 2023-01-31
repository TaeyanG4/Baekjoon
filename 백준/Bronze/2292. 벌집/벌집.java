import java.util.*;
import java.io.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int inputValue = sc.nextInt();
        int sum = 1;
        int num = 1;
        for (int i = 0; sum < inputValue; i++) {
            if(inputValue == 1) break;
            sum += i*6; //6각형 1변의 크기를 6개 전부 더함
            num++; // 변크기가 늘어날떄마다 num에 더하기
        }
        if(inputValue == 1) {
            System.out.println(num);
        }
        else{
            System.out.println(num-1);
        }
    }
}
