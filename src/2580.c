/*
아홉 줄에 걸쳐 한 줄에 9개씩 게임 시작 전 스도쿠판 각 줄에 쓰여 있는 숫자가 한 칸씩 띄워서 차례로 주어진다. 
스도쿠 판의 빈 칸의 경우에는 0이 주어진다. 스도쿠 판을 규칙대로 채울 수 없는 경우의 입력은 주어지지 않는다.

모든 빈 칸이 채워진 스도쿠 판의 최종 모습을 아홉 줄에 걸쳐 한 줄에 9개씩 한 칸씩 띄워서 출력한다.
스도쿠 판을 채우는 방법이 여럿인 경우는 그 중 하나만을 출력한다.

ex.
input
0 3 5 4 6 9 2 7 8
7 8 2 1 0 5 6 0 9
0 6 0 2 7 8 1 3 5
3 2 1 0 4 6 8 9 7
8 0 4 9 1 3 5 0 6
5 9 6 8 2 0 4 1 3
9 1 7 6 5 2 0 8 0
6 0 3 7 0 1 9 5 2
2 5 8 3 9 4 7 6 0

output
1 3 5 4 6 9 2 7 8
7 8 2 1 3 5 6 4 9
4 6 9 2 7 8 1 3 5
3 2 1 5 4 6 8 9 7
8 7 4 9 1 3 5 2 6
5 9 6 8 2 7 4 1 3
9 1 7 6 5 2 3 8 4
6 4 3 7 8 1 9 5 2
2 5 8 3 9 4 7 6 1


good test case:
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


