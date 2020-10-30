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
