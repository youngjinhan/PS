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
	int ring[100], N;
	scanf("%d", &N);
	for (int i = 0; i < N; i++)
		scanf("%d", &ring[i]);

	for (int i = 1; i < N; i++)
		printf("%d/%d\n", ring[0] / gcd(ring[0], ring[i]), ring[i] / gcd(ring[0], ring[i]));
	
	return 0;
}
