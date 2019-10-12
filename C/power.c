/* This program calculates the Power of the Number with a complexity of O(log n). It implements a Recurssive Function which divides
the power by 2 each time it is called and if the power is even then a product of the value retrieved through Recursive Function is returned
and if Odd then a prooduct of the value retrieved through Recursive Function along with the number itself is returned. For example if the 
number is 7 and power is 6: Then 6 will be divided by 2 and will be passed to the same function with the number being 6 and root being 3. */

#include <stdio.h>
#include <conio.h>
float pow(float a,int b); //To Calculate the Power of the Number
void main() //main() function starts
{
float a;
int b;
printf("Enter the number: \n");
scanf("%f",&a);
printf("Enter the power: \n");
scanf("%d",&b);
float c=0.0;
c=(float)pow(a,b); //Calculating the Power of the Number
printf("The Result is %f",c);
getch();
}
float pow(float a,int b)
{
float result;
if(b==0) //If the Power is 0, then 1 is returned
{
return 1;
}
else
{
result=pow(a,b/2); //Calling the Function Recursively
if(b%2==0)
return result*result;
else
return result*result*a;
}
} //Program Ends
