/* brute force 알고리즘을 이용하여
    1부터 N-1까지 1씩 증가하며 N이 해당하는 숫자의 생성자인지 확인한다.
*/

#include <stdio.h>
#pragma warning(disable:4996)

int main()
{
    int N, i, tmp, div, ex=0;

    scanf("%d", &N);

    for (i = 1; i < N; i++)
    {
        tmp = i + i % 10;
        div = i / 10;
        while (div != 0)
        {
            tmp += div % 10;
            div /= 10;
        }

        if (tmp == N)
        {
            ex = 1;
            printf("%d", i);
            break;
        }
    }

    if (ex == 0)
        printf("0");

    return 0;
}
