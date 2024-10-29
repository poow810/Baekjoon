class Solution {
    public int[] solution(String[] keyinput, int[] board) {
        int n = (board[0] - 1) / 2;
        int m = (board[1] - 1) / 2;
        
        int startX = 0;
        int startY = 0;

        for (String a : keyinput) {
            if (a.equals("left") && startX - 1 >= -n) {
                startX--;
            } else if (a.equals("right") && startX + 1 <= n) {
                startX++;
            } else if (a.equals("up") && startY + 1 <= m)  {
                startY++;
            } else if (a.equals("down") && startY -1 >= -m) {
                startY--;
            }
        }
        
        int[] answer = {startX, startY};
        
        return answer;
    }
}