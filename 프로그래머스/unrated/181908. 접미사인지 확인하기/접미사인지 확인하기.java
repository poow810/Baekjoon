class Solution {
    public int solution(String my_string, String is_suffix) {
        StringBuilder sb = new StringBuilder();
        if (my_string.length() < is_suffix.length()) {
            return 0;
        }
        int index = my_string.length() - is_suffix.length();

        for (int i = index; i < my_string.length(); i++) {
            sb.append(my_string.charAt(i));
        }
        if (sb.toString().equals(is_suffix)) {
            return 1;
        }
        return 0;
    }
}   