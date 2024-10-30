class Solution {
    public int solution(String A, String B) {
        int n = A.length();
        int count = 0;
        int answer = 0;
        while (count < n) {
            if (A.equals(B)) {
                return answer;
            }
            
            String temp = A.substring(n - 1);
            A = temp + A.substring(0, n - 1);
            answer++;
            count++;
        }
        
        return -1;
    }
}