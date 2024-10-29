class Solution {
    public int solution(int[][] dots) {
        int x1 = Integer.MAX_VALUE;
        int x2 = Integer.MIN_VALUE;
        
        int y1 = Integer.MAX_VALUE;
        int y2 = Integer.MIN_VALUE;
        
        for (int a = 0; a < dots.length; a++) {
            if (x1 > dots[a][0]) x1 = dots[a][0];
            if (x2 < dots[a][0]) x2 = dots[a][0];
            if (y1 > dots[a][1]) y1 = dots[a][1];
            if (y2 < dots[a][1]) y2 = dots[a][1];
        }
        
        return (x1-x2)*(y1-y2);
    }
}