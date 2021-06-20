/* brute force 알고리즘을 이용하여 모든 경우의 수 계산.
  중간에 M과 같은 값이 나올 시 바로 출력
/*

#include <stdio.h>
#pragma warning(disable:4996)

int main()
{
    int N, M, *card;
    int i, j, k, tmp, ans = 0, fin = 0;
    scanf("%d %d", &N, &M);

    card = (int*)malloc(sizeof(int) * N);

    for (i = 0; i < N; i++)
        scanf("%d", &card[i]);
        
    for (i = 0; i < N; i++)
    {
        if (fin == 1)
            break;
        for (j = i+1; j < N; j++)
        {
            if (fin == 1)
                break;
            for (k = j + 1; k < N; k++)
            {
                tmp = card[i] + card[j] + card[k];
                if (tmp == M) 
                {
                    fin = 1;
                    ans = tmp;
                    break;
                }
                    
                if (tmp <= M && tmp > ans)
                {
                    ans = tmp;
                }
            }
        }
    }

    printf("%d", ans);

    free(card);

    return 0;
}
