#include <stdio.h>

int gcd(int a, int b)
{
	if (a < b)
	{
		int tmp = a;
		a = b;
		b = tmp;
	}

	while (a % b != 0)
	{
		int tmp = a % b;
		a = b;
		b = tmp;
	}
	
	return b;
}

int main()
{
	int num[101], M=1000000000, i;
	int N;
	scanf("%d", &N);
	for (int i = 0; i < N; i++)
	{
		scanf("%d", &num[i]);
	}
		
	for (int i = 0; i < N-1; i++)
	{
		if (num[i] < num[i + 1])
			num[i] = num[i + 1] - num[i];
		else
			num[i] -= num[i + 1];
	}

	if (N == 2)
		M = num[0];
	else
	{
		for (int i = 1; i < N - 1; i++)
		{
			if (i == 1)
			{
				M = gcd(num[0], num[1]);
			}


			else
				M = gcd(num[i], M);
		}
	}
	

	for (i = 2; i * i <= M; i++)
	{
		if (M % i == 0)
		{
			printf("%d ", i);
		}
		
	}

	for (i=i-1; i >= 1; i--)
	{
		if(i*i!=M)
		{ 
			if (M % i == 0)
			{
				if(M/i!=1)
					printf("%d ", M / i);
			}
					
			
		}
	}
	return 0;
}
