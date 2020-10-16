#include <stdio.h>
#pragma warning(disable:4996)

int n, i, j;

void star(int row, int column, int num)
{
    if ((row / num) % 3 == 1 && (column / num) % 3 == 1)
        printf(" ");
    else
    {
        if (num == 1)
            printf("*");
        else
            star(row, column, num/3);
    }

}
        

int main()
{
    scanf("%d", &n);

    for (i = 0; i < n; i++)
    {
        for (j = 0; j < n; j++)
        {
            star(i, j, n);
        }
        printf("\n");
    }
        
    

    return 0;
}
