class Solution {
    public int solution(int order) {
        int answer = 0;
        for (int a : String.valueOf(order).toCharArray()) {
            if (a == '3' || a == '6' || a == '9') {
                answer++;
            }
        }
        return answer;
    }
}