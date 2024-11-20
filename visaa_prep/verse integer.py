#include <stdio.h>
#include <limits.h>
int reverse(int n) {
    int reversed = 0;

    while (n != 0) {
        int digit = n % 10;
        n /= 10;


        if (reversed > INT_MAX / 10 || (reversed == INT_MAX / 10 && digit > INT_MAX % 10)) {
            return 0;          }
        if (reversed < INT_MIN / 10 || (reversed == INT_MIN / 10 && digit < INT_MIN % 10)) {
            return 0;  
        }

        reversed = reversed * 10 + digit;
    }

    return reversed;
}

int main() {
    int n;
    scanf("%d", &n);  


    printf("%d\n", reverse(n));

    return 0;
}
