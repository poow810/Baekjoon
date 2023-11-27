class Solution {
    public int solution(int n, String control) {
        int answer = n;


        for (char x : control.toCharArray()) {
            if (x == 'w') {
                answer += 1;
            }
            if (x == 's') {
                answer -= 1;
            }
            if (x == 'd') {
                answer += 10;
            }
            if (x == 'a') {
                answer -= 10;
            }
        }
        return answer;
    }
}