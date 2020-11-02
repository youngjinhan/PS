// 666이 들어간 N번째 숫자 찾기
// ex1. 입력: 2 출력: 1666
// ex2. 입력: 6 출력: 5666
// ex3. 입력: 7 출력: 6660

#include <stdio.h>
#pragma warning(disable:4996)

int main()
{
    int N,count=0, div, i;

    scanf("%d", &N);

    for (i = 665;; i++)
    {
        if (i % 1000 == 666)
        {
            count++;
            if (N == count)
                break;
        }

        else if (i > 1000)
        {
            div = i;
            while (div != 0)
            {
                div /= 10;
                if (div % 1000 == 666)
                {
                    count++;
                    break;
                }
            }
            
            if (N == count)
                break;

        }
        
       
        

    }
    printf("%d", i);
    return 0;
}
