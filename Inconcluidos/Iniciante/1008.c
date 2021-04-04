#include <stdio.h>
 
int main() {
 
    int numFunc, numTrab;
    double valor;
    scanf("%i",&numFunc);
    scanf("%i",&numTrab);
    scanf("%lf",&valor);
    printf("NUMBER = %i\n",numFunc);
    printf("SALARY = U$ %.2lf\n",(numTrab*valor));
 
    return 0;
}