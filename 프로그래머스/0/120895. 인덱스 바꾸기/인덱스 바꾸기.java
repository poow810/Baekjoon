class Solution {
    public StringBuilder solution(String my_string, int num1, int num2) {
        char num_str1 = my_string.toCharArray()[num1];
        char num_str2 = my_string.toCharArray()[num2];

        StringBuilder answer = new StringBuilder();

        for (int i = 0; i < my_string.length(); i++) {
            if (i == num1) {
                answer.append(num_str2);
            } else if (i == num2) {
                answer.append(num_str1);
            } else {
                answer.append(my_string.charAt(i));
            }
        }
        return answer;
    }
}