#include <stdio.h>

int main() {
    long long X, Y;

    scanf("%lld %lld", &X, &Y);

     if (X >= Y) {
        printf("YES\n");
    } else {
        printf("NO\n");
    }

    return 0;
}
