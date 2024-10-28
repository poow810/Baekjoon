class Solution {
    public String solution(String rny_string) {
        String answer = "";
        
        for (char x: rny_string.toCharArray()) {
            if (x == 'm') {
                answer += "rn";
            } else {
                answer += x;
            }
        }
        
        return answer;
    }
}