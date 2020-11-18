/*
자연수 N과 M이 주어졌을 때(1 ≤ M ≤ N ≤ 7), 1부터 N까지 자연수 중에서 중복을 허용하여 M개를 고른 수열을 오름차순으로 출력.

ex1.
input
4 2

output
1 1
1 2
1 3
1 4
2 1
2 2
2 3
2 4
3 1
3 2
3 3
3 4
4 1
4 2
4 3
4 4

ex2.
input
3 3

output
1 1 1
1 1 2
1 1 3
1 2 1
1 2 2
1 2 3
1 3 1
1 3 2
1 3 3
2 1 1
2 1 2
2 1 3
2 2 1
2 2 2
2 2 3
2 3 1
2 3 2
2 3 3
3 1 1
3 1 2
3 1 3
3 2 1
3 2 2
3 2 3
3 3 1
3 3 2
3 3 3
*/

#include <stdio.h>

int out[10];
int N, M;

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
		//printf("%d ",out[cur]);
		sol(cur + 1);
				
	}
	//printf("\n");
	
}


int main()
{
	
	scanf("%d %d", &N, &M);
	sol(1);
	return 0;

}


