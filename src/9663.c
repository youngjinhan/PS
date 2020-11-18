/*
크기가 N × N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제이다.
N이 주어졌을 때 (1 ≤ N < 15), 퀸 N개를 서로 공격할 수 없게 놓는 경우의 수를 출력한다.

ex1.
input
4

output
2

ex2.
input
8

output
92
*/

#include <stdio.h>

int out[16];
int N,count=0;


int isGood(int cur)
{
	for (int i = 1; i < cur; i++)
	{
		if(cur>1)
			if (out[i] == out[cur] || out[i] + i == out[cur] + cur || cur-i==out[cur]-out[i])
				return 0;
	}

	return 1;
}


void sol(int cur)
{
	if (cur > N)
	{
		/*for (int i = 1; i <= N; i++)
			printf("%d ", out[i]);
		printf("\n");*/
		count++;
		return;
	}

	for (int i = 1; i <= N; i++)
	{
		out[cur] = i;
		if (isGood(cur))
		{
			//printf("%d ", out[cur]);
			sol(cur + 1);
		}
				
	}
	//printf("\n");
	
}


int main()
{
	
	scanf("%d", &N);
	sol(1);
	printf("%d", count);
	return 0;

}


