class Solution {
    public int solution(String myString, String pat) {
        String str = "";
        for (char x : myString.toCharArray()) {
            if (x == 'A') {
                str += 'B';
            } else {
                str += 'A';
            }
        }
        
        if (str.contains(pat)) {
            return 1;
        } else {
            return 0;
        }
    }
}