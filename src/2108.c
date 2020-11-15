// 첫째줄에 줄의 개수 N개가 주어지고

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
