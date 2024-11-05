class Solution {
    public int solution(int[] numbers) {
        int answer = Integer.MIN_VALUE;
        for (int a = 0; a < numbers.length; a++) {
            for (int b = 0; b < numbers.length; b++) {
                if (a == b) {
                    continue;
                }
                if (answer < numbers[a]*numbers[b]) {
                    answer = numbers[a]*numbers[b];
                }
            }
        }
        return answer;
    }
}