#include <stdio.h>
#include <stdlib.h>
#pragma warning(disable:4996)



int main()
{
    char* string;
    int i, N, tmp, sum = 0;

    scanf("%d", &N);
    string = (char*)malloc(sizeof(char) * N);
    
    scanf("%s", string);
   

    for (i = 0; i < N; i++)
    {
        tmp = string[i] - '0';
        sum += tmp;
    }
    printf("\n");
    printf("%d", sum);

    return 0;

}
