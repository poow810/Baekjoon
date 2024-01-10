import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int num = Integer.parseInt(br.readLine());

        st = new StringTokenizer(br.readLine());
        int min = 0, max = 0;
        for (int i = 0; i < num; i++) {
            int can = Integer.parseInt(st.nextToken());
            if(i == 0) {
                min = can;
                max = can;
                continue;
            }
            if (can < min) {
                min = can;
            }
            if (can > max) {
                max = can;
            }
        }
        System.out.println(min+" "+ max);
    }
}