#include <stdio.h>
#include <stdlib.h>
#pragma warning(disable:4996)

int arr[1000001];

// 오름차순으로 정렬할 때 사용하는 비교함수
int static compare(const void* first, const void* second)
{
    if (*(int*)first > * (int*)second)
        return 1;
    else if (*(int*)first < *(int*)second)
        return -1;
    else
        return 0;
}

int main()
{
    
    
    int i, N;

    scanf("%d", &N);
    for (i = 0; i < N; i++)
    {
        scanf("%d", &arr[i]);
    }
    qsort(arr, N, sizeof(int), compare);

    // 정렬 후
    for (i = 0; i < N; i++) printf("%d\n", arr[i]);
    printf("\n");

    return 0;
}
