class Solution {
    public int solution(int n) {
        int divide = 6;
        int answer = 0;
        while(true) {
            if (divide % n == 0) {
                answer++;
                return answer;
            } else {
                divide += 6;
                answer++;
            }
        }
    }
}