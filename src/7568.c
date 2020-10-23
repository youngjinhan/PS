/*
    모든 기본 순위를 1위로 설정하여
    brute force 알고리즘을 이용하여
    덩치가 작고 큰것이 판별될 시 작은 사람의 순위를 1씩 추가하여 결과 
*/

#include <stdio.h>
#pragma warning(disable:4996)

int main()
{
    int info[51][3], N, i,j;

    scanf("%d", &N);
    for (i = 0; i < N; i++)
    {
        scanf("%d %d", &info[i][0], &info[i][1]);
        info[i][2] = 1;
    }

    for (i = 0; i < N; i++)
    {
        for (j = i + 1; j < N; j++)
        {
            if (info[i][0] > info[j][0] && info[i][1] > info[j][1])
                info[j][2]++;

            else if (info[i][0] < info[j][0] && info[i][1] < info[j][1])
                info[i][2]++;
        }
    }

    for (i = 0; i < N; i++)
        printf("%d ", info[i][2]);


    return 0;
}
