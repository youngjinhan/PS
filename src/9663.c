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


