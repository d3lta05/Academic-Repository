// file I created to target and reverse-engineer with Ghidra as a small personal project

#include <stdio.h>
#include <math.h>
#include <stdlib.h>

int testFunction(int a, int b) {
    double c = sqrt((a * b) / 3.14159265);
    return c;
}

int main(void) {
    int a, b;
    scanf("%d %d", &a, &b);
    int result = (testFunction(a, b));
    printf("%d", result);
    printf("%d", &result);
    return 0;
}
