// 주어진 수의 자리수를 내림차순으로 정렬하기

/* ex.
input
2413

output
4321
*/

#include <stdio.h>
#include <stdlib.h>
#pragma warning(disable:4996)


void swap(int *arr, int a, int b) {
    arr[a] = arr[a] ^ arr[b];
    arr[b] = arr[a] ^ arr[b];
    arr[a] = arr[a] ^ arr[b];
}

int main()
{
    char string[11];
    int num[11], i, N, tmp;
    
    scanf("%s", string);

    for (i = 0; i < 11; i++)
    {
        if (string[i] == NULL)
        {
            N = i;
            break;
        }
            
    }
   
    for (i = 0; i < N; i++)
    {
        tmp = string[i] - '0';
        num[i]= tmp;
    }


    for (i = 0; i < N - 1; i++)
    {
        for (int j = i + 1; j < N; j++)
        {
            if (num[i] < num[j])
            {
                swap(num,i, j);
            }
        }
    }

    for (i = 0; i < N; i++)
        printf("%d", num[i]);
    

    return 0;

}
