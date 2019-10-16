#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
	
    int n,a;
    scanf("%d", &n);
    int num=n;
    int sum=0;
    while(num>0){
        a=num%10;
        sum=sum+a;
        num=num/10;
        }
    //Complete the code to calculate the sum of the five digits on n.
    printf("%d",sum);
    return 0;
}

