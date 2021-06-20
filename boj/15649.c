/*
자연수 N과 M이 주어졌을 때, 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 모든 수열 출력하기.
첫째 줄에 자연수 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 8)
한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다. 중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.
수열은 사전 순으로 증가하는 순서로 출력해야 한다.

ex1.
input
3 1

output
1
2
3

ex2.
input
4 2

output
1 2
1 3
1 4
2 1
2 3
2 4
3 1
3 2
3 4
4 1
4 2
4 3
*/

#include <stdio.h>

int out[10], N, M;

int isGood(int cur)
{
	for (int i = 1; i < cur; i++)
	{
		if (out[cur] == out[i])
			return 0;
	}
	return 1;
}

void sol(int cur)
{
	if (cur > M) 
	{
		for (int i = 1; i <= M; i++)
			printf("%d ", out[i]);
		printf("\n");
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
		//printf("\n");
	}
	
}


int main()
{

	scanf("%d %d", &N, &M);
	sol(1);
	
		
	
	return 0;

}
