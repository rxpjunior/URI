#include <stdio.h>
 
int main() {
 
   int codpeca1, quantpeca1, codpeca2, quantpeca2;
    double vpeca1,vpeca2;
    scanf("%i %i %lf",&codpeca1,&quantpeca1,&vpeca1);
    scanf("%i %i %lf",&codpeca2,&quantpeca2,&vpeca2);
    printf("VALOR A PAGAR: R$ %.2lf\n",((quantpeca1*vpeca1)+(quantpeca2*vpeca2)));
 
    return 0;
}