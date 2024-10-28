import java.util.*;

class Solution {
    public List<String> solution(String[] strArr) {
        List<String> answer = new ArrayList<>();
        for (int x = 0; x < strArr.length; x++) {
            if (x % 2 == 0) {
                answer.add(strArr[x].toLowerCase());
            } else {
                answer.add(strArr[x].toUpperCase());
            }
        }
        return answer;
    }
}