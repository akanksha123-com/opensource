#include <stdio.h>

int main() {
    int n, m, num1 = 0, num2 = 0;
    scanf("%d %d", &n, &m);
    
    for (int i = 0; i < n; i++) {
        int num;
        scanf("%d", &num);
        
        if (num % m == 0) {
            num1 += num;  
        } else {
            num2 += num;
        }
    }
    
    printf("%d\n", num1 - num2);  
    return 0;
}
