#include <stdio.h>
 
int main() {
 
    int a,b,c,d,prod1, prod2;
    scanf("%i",&a);
    scanf("%i",&b);
    scanf("%i",&c);
    scanf("%i",&d);
    prod1=a*b;
    prod2=c*d;
    printf("DIFERENCA = %i\n",prod1-prod2);
 
    return 0;
}