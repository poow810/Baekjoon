import java.util.*;

class Solution {
    public int[] solution(int[][] score) {
        Double[] avgScore = new Double[score.length];
        int n = 2;

        for (int a = 0; a < score.length; a++) {
            int sum = 0;
            for (int b = 0; b < n; b++) {
                sum += score[a][b];
            }
            avgScore[a] = (double) sum / n;
        }

        int[] result = new int[score.length];

        List<Double> list = new ArrayList<>(Arrays.asList(avgScore));
        Collections.sort(list, Collections.reverseOrder());

        for (int i = 0; i < score.length; i++) {
            result[i] = list.indexOf(avgScore[i]) + 1;
        }
        
        return result;
    }
}
