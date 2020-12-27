/*
첫번째 줄에 숫자 N이 주어지고, 다음 줄부터 N개의 줄에 숫자가 하나씩 주어진다. (2 ≤ N ≤ 100)
이 수는 모두 1보다 크거나 같고, 1,000,000,000보다 작거나 같은 자연수이다.
같은 수가 두 번 이상 주어지지 않는다.
항상 M이 하나 이상 존재하는 경우만 입력으로 주어진다.

첫째 줄에 가능한 M을 공백으로 구분하여 모두 출력한다. 이때, M은 증가하는 순서이어야 한다. (M > 1)

ex.
input
3
6
34
38

output
2 4
*/

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
