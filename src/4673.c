#include <stdio.h>

int main()
{
    int self = 1;
    for (int i = 1; i <= 10000; i++)
    {
        self = 1;
        for (int j = i-1; j > 0; j--)
        {
            if (j < 10)
            {
                if (2 * j == i)
                {
                    self--;
                    break;
                }
            }
            else if(j < 100)
            {
                if (j + j % 10 + j / 10 == i)
                {
                    self--;
                    break;
                }
            }
            else if (j < 1000)
            {
                if (j + j % 10 + (j / 10)%10 + j/100 == i)
                {
                    self--;
                    break;
                }
            }
            else if (j < 10000)
            {
                if (j + j % 10 + (j / 10) % 10 + (j / 100)%10 + j/1000 == i)
                {
                    self--;
                    break;
                }
            }
        }

        if (self)
            printf("%d\n", i);
    }
    return 0;
}
