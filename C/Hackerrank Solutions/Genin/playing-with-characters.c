#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() 
{
    char ch,s[100],sen[100];
    scanf("%c",&ch);
   scanf(" %[^\n]s",s); //  in palce of scanf("%s", &s);
   scanf(" %[^\n]s",sen); // in palce of scanf(" %[^\n]%*c", &sen);
    printf("%c\n%s\n",ch,s);
    printf("%s",sen);
    
        return 0;
}

