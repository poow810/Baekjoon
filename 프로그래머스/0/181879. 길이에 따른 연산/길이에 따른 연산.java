class Solution {
    public int solution(int[] num_list) {
        if (num_list.length >= 11) {
            int answer = 0;
            for (int a : num_list) {
                answer += a;
            }
            return answer;
        } else {
            int answer = 1;
            for (int a : num_list) {
                answer *= a;
            }
            return answer;
        }
    }
}