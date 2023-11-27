class Solution {
    public int solution(int a, int b) {
        String ab = a+""+b;
        String ba = b+""+a;

        if (Integer.parseInt(ab)>Integer.parseInt(ba)) {
            return Integer.parseInt(ab);
        }
        if (Integer.parseInt(ba)>Integer.parseInt(ab)) {
            return Integer.parseInt(ba);
        }
        return Integer.parseInt(ab);
    }
}