class Solution {
    public int solution(int[] arr1, int[] arr2) {
        int add1 = 0;
        int add2 = 0;
        if (arr1.length > arr2.length) {
            return 1;
        } else if (arr1.length < arr2.length) {
            return -1;
        } else {
            for (int i = 0; i < arr1.length; i++) {
                add1 += arr1[i];
                add2 += arr2[i];
            }

            if (add1 > add2) {
                return 1;
            } else if (add1 < add2) {
                return -1;
            } else {
                return 0;
            }
        }
    }
}