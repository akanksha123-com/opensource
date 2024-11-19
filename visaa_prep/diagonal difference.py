import java.util.Scanner;

public class DiagonalDifference {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int primary = 0, secondary = 0;
        
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                int value = sc.nextInt();
                if (i == j) primary += value; 
                if (i + j == n - 1) secondary += value;
            }
        }
        
        System.out.println(Math.abs(primary - secondary));
    }
}
