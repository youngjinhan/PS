// method 1
// 공백을 먼저 처리
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



//method2
// '*'를 먼저 

/*
#include <stdio.h>
#pragma warning(disable:4996)

char list[2200][2200];
int n;

// ******중요******
// i, j, div는 전역변수가 아니라 지역변수로 설정해야함.
void star(int y, int x, int n) {
   
    if (n == 1)
    {
        list[y][x]= '*';
  
    }

    else
    { 
 
        int div = n / 3;
        for (int i = 0; i < 3; i++) 
        {
            for (int j = 0; j < 3; j++) 
            {
                if (i == 1 && j == 1)
                {

                }
                                    
                else
                {
                    star(y+(i*div),x+(j*div),div);
                    
                }
            }
        }
        
    }
}
        


int main()
{
    scanf("%d", &n);

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            list[i][j] = ' ';
        }
    }

    star(0, 0, n);
    for (int i = 0; i < n; i++) 
    {
        for (int j = 0; j < n; j++)
        {
            printf("%c", list[i][j]);
        }
        printf("\n");
    }
   

    return 0;
}
*/
