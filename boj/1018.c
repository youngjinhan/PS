/*
    brute force 알고리즘을 이용
    가능한 8*8을 다 잘라내어 필요로 하는 색칠 횟수를 구한 뒤, 그 중 최소 색칠 횟수를 출력
*/

#include <stdio.h>
#pragma warning(disable:4996)

int main()
{
    char board[51][51],tmp[8][8], cur;
    int N, M, i, j, k, l,count,change;

    scanf("%d %d", &N, &M);
    for (i = 0; i < N; i++)
    {
        for (j = 0; j < M; j++)
        {
            scanf(" %c", &board[i][j]);
        }
    }


    change = 47;
    for (i=0; i + 7 < N; i++)
    {
        for (j=0; j + 7 < M; j++)
        {
            for (k = i; k < i+8; k++)
            {
                for (l = j; l < j + 8; l++)
                {
                    tmp[k - i][l - j] = board[k][l];
                   /* if (board[k][l] == 'B')
                    {
                        if (board[k][l + 1] == 'W')
                        {
                        }
                        else
                        {
                            board[k][l + 1] = 'W';
                            change = 1;
                        }
                    }

                    else
                    {
                        if (board[k][l + 1] == 'B')
                        {
                        }
                        else
                        {
                            board[k][l + 1] = 'B';
                            change = 1;
                        }
                    }*/
                }
                               
            }

            count = 0;
            for (k = 0; k < 8; k++)
            {
                for (l = 0; l < 8; l++)
                {
                    if (k == 0 && l == 0) {
                        cur = tmp[k][l];
                        continue;
                    }
                    if (cur == tmp[k][l])
                    {
                        count += 1;
                        
                    }
                    if (cur == 'B')
                        cur = 'W';
                    else
                        cur = 'B';
                }
                if (cur == 'B')
                    cur = 'W';
                else
                    cur = 'B';
            }
            

            if (count > 32)
                count = 64 - count;

            //printf("%d\n", count);

            if (count < change) {
                change = count;
            }



            
        }
    }

    printf("%d", change);

   


    return 0;
}
