class Solution {
    public int solution(int num, int k) {
        String numStr = String.valueOf(num);
        
        for (int a = 0; a < numStr.length(); a++) {
            if (numStr.charAt(a) -'0' == k) {
                return a+1;
            }
        }
        return -1;
    }
}