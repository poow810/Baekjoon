class Solution {
    public int[] solution(int[] array) {
        int max_num = Integer.MIN_VALUE;
        int index = 0;
        
        for (int i = 0; i < array.length; i++) {
            if (max_num < array[i]) {
                max_num = array[i];
                index = i;
            }
        }
        int[] answer = {max_num, index};
        return answer;
    }
}