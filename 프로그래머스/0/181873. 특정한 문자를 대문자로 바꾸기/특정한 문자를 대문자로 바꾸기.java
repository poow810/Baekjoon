class Solution {
    public String solution(String my_string, String alp) {
        String answer = "";
        for (char x : my_string.toCharArray()) {
            if (Character.toString(x).equals(alp)) {
                answer += Character.toString(x).toUpperCase();
            } else {
                answer += x;
            }
        }
        return answer;
    }
}