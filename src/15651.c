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


