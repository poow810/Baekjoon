import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);
        String string;
        string = scanner.nextLine().trim();
        if (string.isEmpty()) {
            System.out.println(0);
        } else {
        List<String> array = Arrays.asList(string.split(" "));
        int count = array.size();
        System.out.println(count);
        }
    }
}
