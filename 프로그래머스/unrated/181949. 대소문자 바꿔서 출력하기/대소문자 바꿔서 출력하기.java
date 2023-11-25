import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String str = sc.next();
        StringBuilder string = new StringBuilder();
        for (char x: str.toCharArray()) {

            if (Character.isLowerCase(x)) {
                string.append(Character.toUpperCase(x));
            }

            if (Character.isUpperCase(x)) {
                string.append(Character.toLowerCase(x));
            }
        }
        System.out.println(string);
    }
}