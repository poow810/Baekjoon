import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<Integer> solution(int[] arr) {
        List<Integer> result = new ArrayList<>();

        for (int a : arr) {
            for (int b = 0; b < a; b++) {
                result.add(a);
            }
        }

        return result;
    }
}