#include <stdio.h>

int main()
{
    int N, count = 0;
    scanf("%d", &N);
    if (N < 100)
        printf("%d\n", N);
    else
    {
        for (int i = 111; i <= N; i++)
        {
            int i100, i10, i1;
            i1 = i % 10;
            i100 = i / 100;
            i10 = (i / 10) % 10;

            if (i10 - i100 == i1 - i10)
                count++;
        }

     
        printf("%d\n", 99 + count);
    }
    return 0;
}
