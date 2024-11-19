import java.util.*;

public class Solution {
    public static List<Integer> createArray(int n) {
        List<Integer> result = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            result.add(i); 
        }
        return result;
    }
    
    public static void main(String[] args) {
       
        int n = 10;
        List<Integer> result = createArray(n);
        System.out.println(result); 
    }
}
