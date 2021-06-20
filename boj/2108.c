/* 
첫째줄에 줄의 개수 N개가 주어지고(1<=N<=500,000) 그 다음 N개의 줄에 정수가 하나씩 주어진다.
이고 입력되는 정수의 절대값은 4,000을 넘지 않는다.

첫째 줄에는 산술평균을 출력한다. 소수점 이하 첫째 자리에서 반올림한 값을 출력한다.
둘째 줄에는 중앙값을 출력한다.
셋째 줄에는 최빈값을 출력한다. 여러 개 있을 때에는 최빈값 중 두 번째로 작은 값을 출력한다.
넷째 줄에는 범위를 출력한다.

ex1.
input
5
1
3
8
-2
2

output
2
2
1
10

ex2.
input
1
4000

output
4000
4000
4000
0

ex3.
input
5
-1
-2
-3
-1
-2

output
-2
-2
-1
2
*/



#include <stdio.h>
#include <math.h>

int count[8001] = { 0, };

int main() {
	
	
    int N, i, sum = 0, max = 0, cnt, freq, tmp, order=0, first,last;
	scanf("%d", &N);

	for (i = 0; i < N; i++)
	{
		scanf("%d", &tmp);
        count[tmp+4000]++;
		sum += tmp;
        
	}

	printf("%d\n", (int)floor((double)sum/(double)N + 0.5));

    for (i = 0; i <= 8000; i++)
    {

        if(order<(N+1)/2)
        {
            order += count[i];
            if (order >= (N+1) / 2)
                printf("%d\n", i - 4000);
        }
        

    }
    
    for (i = 0; i <= 8000; i++)
    {
        
        if (max < count[i])
            max = count[i];
    }

    cnt = 0;
    for (i = 0; i <= 8000; i++)
    {
        if (max == count[i])
        {
            cnt++;
            freq = i;
        }

    }

    if (cnt == 1)
    {
        printf("%d\n", freq - 4000);

    }
    else
    {
        cnt = 0;
        for (i = 0; i <= 8000; i++)
        {
            if (max == count[i]) {
                if (++cnt == 2)
                {
                    printf("%d\n", i - 4000);
                    break;
                }
            }
        }

    }

    for (i = 0; i <= 8000; i++)
    {
        if (count[i] != 0)
        {
            first = i - 4000;
            break;
        }
    }
        
    for (i = 8000; i >= 0; i--)
    {
        if (count[i] != 0)
        {
            last = i - 4000;
            break;
        }
    }
    

    printf("%d\n", last - first);


	return 0;
}
