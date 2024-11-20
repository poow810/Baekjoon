import java.util.*;

class Solution {
    public int[] solution(String my_string) {
        Map<String, Integer> friends = new HashMap<>();
        friends.put("0", 0);
        friends.put("1", 1);
        friends.put("2", 2);
        friends.put("3", 3);
        friends.put("4", 4);
        friends.put("5", 5);
        friends.put("6", 6);
        friends.put("7", 7);
        friends.put("8", 8);
        friends.put("9", 9);

        List<Integer> answer = new ArrayList<>();
        for (char a : my_string.toCharArray()) {
            if (friends.containsKey(String.valueOf(a))) {
                answer.add(friends.get(String.valueOf(a)));
            }
        }
        answer.sort(Integer::compareTo);
        return answer.stream().mapToInt(Integer::intValue).toArray();
    }
}