// N개의 수 정렬하기 2 - 오름차순
// 1<=N<=1,000,000
// 첫째줄에 개수 N개, 두번째 줄부터 숫자 N개가 주어짐

/*
ex.
input
5
5
4
3
2
1

output
1
2
3
4
5
*/


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
