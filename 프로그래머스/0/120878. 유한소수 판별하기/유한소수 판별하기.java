class Solution {
    public int solution(int a, int b) {
        b /= gcd(a, b);
        
        if (factorize(b)) return 1;
        return 2;
    }
    
    static int gcd(int a, int b) {
        if (b == 0) {
            return a;
        }
        return gcd(b, a % b);
    }
    
    static boolean factorize(int n) {
        boolean result = true;
        
        while (n > 1) {
            for (int i = 2; i <= n; i++) {
                if (n % i == 0) {  // n이 i로 나누어지면
                    n /= i;  // n을 i로 나누어 줄임
                    if (i != 2 && i != 5)  // i가 2나 5가 아니면
                        return false;  // 유한소수가 아님
                    break;  // 다음 소인수로 넘어가기
                }
            }
        }
        return result;  // 모든 소인수가 2와 5라면 true 반환
    }
}