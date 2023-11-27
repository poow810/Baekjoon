class Solution {
    public int[] solution(int[] num_list) {
        int[] answer = new int[num_list.length + 1];
        int index = num_list.length;
        System.arraycopy(num_list, 0, answer, 0, index);
        if (num_list[index-1] > num_list[index-2]) {
            answer[index] = num_list[index-1] - num_list[index-2];
            return answer;
        }
        if (num_list[index-1] <= num_list[index-2]) {
            answer[index] = num_list[index-1] * 2;
            return answer;
        }
        return num_list;
    }
}