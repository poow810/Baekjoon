class Solution {
    public int solution(String num_str) {
        int answer = 0;
        for (char x : num_str.toCharArray()) {
            answer += Integer.parseInt(String.valueOf(x));
        }
        return answer;
    }
}