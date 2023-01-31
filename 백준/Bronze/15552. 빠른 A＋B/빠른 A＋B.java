import java.io.*;
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int t = Integer.parseInt(br.readLine());

        int a,b;

        for(int i = 0; i<t; i++){
    String line = br.readLine();
    int index = line.indexOf(' ');
            a = Integer.parseInt(line.substring(0, index));
            b = Integer.parseInt(line.substring(index+1, line.length()));
            bw.write(String.valueOf(a+b));
            bw.write('\n');
            
        }
        bw.flush();
        bw.close();
    }
}