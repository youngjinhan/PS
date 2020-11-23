/*
test case:
0 2 0 9 0 5 0 0 0
5 9 0 0 3 0 2 0 0
7 0 0 6 0 2 0 0 5
0 0 9 3 5 0 4 6 0
0 5 4 0 0 0 7 8 0
0 8 3 0 2 7 5 0 0
8 0 0 2 0 9 0 0 4
0 0 5 0 4 0 0 2 6
0 0 0 5 0 3 0 7 0

answer: (check it)
+-----+-----+-----+
|3 2 1|9 7 5|6 4 8|
|5 9 6|8 3 4|2 1 7|
|7 4 8|6 1 2|9 3 5|
+-----+-----+-----+
|1 7 9|3 5 8|4 6 2|
|2 5 4|1 9 6|7 8 3|
|6 8 3|4 2 7|5 9 1|
+-----+-----+-----+
|8 1 7|2 6 9|3 5 4|
|9 3 5|7 4 1|8 2 6|
|4 6 2|5 8 3|1 7 9|
+-----+-----+-----+
*/

#include <stdio.h>

int sudoku[10][9], count=0;


int isGood(int x, int y)
{
			
	for (int i = 0; i < 9; i++)
	{
		
		if(i != y && sudoku[x][i] == sudoku[x][y])
			return 0;
		if (i != x && sudoku[i][y] == sudoku[x][y])
			return 0;
		
	}

	int square_x, square_y;
	square_x = x / 3;
	square_y = y / 3;
	
	
		

	for (int i = 0; i < 3; i++)
	{
		for (int j = 0; j < 3; j++)
		{
			if (x == i + (square_x * 3) && y == j + (square_y * 3))
				continue;

			if (sudoku[x][y] == sudoku[(square_x * 3) + i][(square_y * 3) + j])
				return 0;

		}
	}

	return 1;
}


void sol(int x, int y)
{
	if (count)
		return;
	

	while (sudoku[x][y] != 0)
	{
		if (y == 8)
		{
			x += 1;
			y = 0;
		}
		else
			y++;
	}
	//printf("%d %d\n", x, y);

	if (x > 8)
	{
		if (count == 0)
		{
			for (int i = 0; i < 9; i++) {
				for (int j = 0; j < 9; j++)
				{
					if (j == 8)
						printf("%d", sudoku[i][j]);
					else
						printf("%d ", sudoku[i][j]);
				}
				printf("\n");
			}
			count++;
		}


		return;
	}

	for (int i = 1; i <= 9; i++)
	{ 
		sudoku[x][y] = i;
		//if (x == 0 && y == 0)
			//printf("%d %d\n", i, sudoku[x][y]);
		if (isGood(x, y))
		{
			//printf("%d %d %d\n", x,y, sudoku[x][y]);
			
			//printf("이자리 좋아 : (%d,%d)=%d\n", x, y,sudoku[x][y]);
			if (y == 8)
			{
				sol(x + 1, 0);
			}
			else
				sol(x, y + 1);
		}
		sudoku[x][y] = 0;
		

	}


		
	

	
}


int main()
{
	for(int i=0;i<9;i++)
		for(int j=0;j<9;j++)
			scanf("%d", &sudoku[i][j]);
	sol(0,0);

	
		
	return 0;

}


