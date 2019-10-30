// https://www.hackerrank.com/challenges/30-data-types/problem

#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
    int i = 4;
    double d = 4.0;
    char s[] = "HackerRank ";

   int num1;
   scanf("%d",&num1);
   double num2;
   scanf("%lf",&num2);
   char str[100],*p,a[100];
    scanf(" %[^\n]",str);
    p=strcpy(a,s);

num1=num1+i;
num2=(double)num2+d;
strcat(s,a);
printf ("%d",num1);
printf("\n");
printf("%.1lf",num2);
printf("\n");
p=strcat(a,str);
    printf("%s\n",p);
   
    return 0;
}
