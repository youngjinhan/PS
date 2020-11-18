#include <stdio.h>

int out[10];
int N, M;


int isGood(int cur)
{
	for (int i = 1; i < cur; i++)
	{
		if (out[cur] < out[i])
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
				
	}
	//printf("\n");
	
}


int main()
{
	
	scanf("%d %d", &N, &M);
	sol(1);
	return 0;

}


