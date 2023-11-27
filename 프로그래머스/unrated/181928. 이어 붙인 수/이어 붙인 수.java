class Solution {
    public int solution(int[] num_list) {
        int answer = 0;
        StringBuilder even = new StringBuilder();
        StringBuilder odd = new StringBuilder();

        for (int num : num_list) {
            if (num % 2 == 0) {
                even.append(num);
            }
            if (num % 2 == 1) {
                odd.append(num);
            }
        }
        answer = Integer.parseInt(even.toString()) + Integer.parseInt(odd.toString());
        return answer;
    }
}