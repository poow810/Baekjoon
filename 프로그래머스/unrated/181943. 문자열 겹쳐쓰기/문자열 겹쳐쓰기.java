class Solution {
    public String solution(String my_string, String overwrite_string, int s) {
        String answer = "";

        for (int i = 0; i < s; i++) {
            char firstChar = my_string.charAt(i);
            String firstString = String.valueOf(firstChar);
            answer += firstString;
        }
        answer += overwrite_string;
        if (my_string.length() > answer.length()) {
            String secondString = my_string.substring(answer.length());
            answer += secondString;
        }
     return answer;
    }
}