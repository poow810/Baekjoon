class Solution {
    public int solution(int a, int b) {
        String addString = ""+a+b;
        int add = Integer.parseInt(addString);
        int multiplication = 2*a*b;
        return Math.max(add, multiplication);
    }
}