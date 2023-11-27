class Solution {
    public String[] solution(String[] names) {
        int groupSize = 5;
        if (names.length < groupSize) {
            return new String[]{names[0]};
        }

        int remainGroupSize = (int) Math.ceil((double) names.length / groupSize);
        String[] answer = new String[remainGroupSize];

        for (int i = 0; i < remainGroupSize; i++) {
            answer[i] = names[i * groupSize];
        }
        return answer;
    }
}