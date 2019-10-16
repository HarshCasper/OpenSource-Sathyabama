#include<stdio.h>

int main(){
    int i, j;
    float f, g;
    scanf("%d %d %f %f", &i, &j, &f, &g);
    printf("%d %d\n%.1f %.1f", i+j, i-j, f+g, f-g);
    return 0;
}
