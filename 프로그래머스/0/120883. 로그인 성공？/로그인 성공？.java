import java.util.*;

class Solution {
    public String solution(String[] id_pw, String[][] db) {
        for (String[] c : db) {
            if (Arrays.equals(c, id_pw)) {
                return "login";
            } else if (id_pw[0].equals(c[0])) {
                return "wrong pw";
            }
        }
        return "fail";
    }
}