/*
두 자연수 A와 B가 주어졌을 때, A와 B의 최소공배수를 구하기
첫째 줄에 테스트 케이스의 개수 T(1 ≤ T ≤ 1,000)가 주어진다. 둘째 줄부터 T개의 줄에 걸쳐서 A와 B가 주어진다. (1 ≤ A, B ≤ 45,000)

ex.
input
3
1 45000
6 10
13 17

output
45000
30
221
*/

#include <stdio.h>

int main()
{
	int out[1001], T;
	scanf("%d", &T);
	for (int i = 0; i < T; i++)
	{
		int a, b, mult;
		scanf("%d %d", &a, &b);
		mult = a * b;
		// a>=b 상태로 만듬
		if (b > a)
		{
			int tmp = b;
			b = a;
			a = tmp;
		}
		while (a % b != 0)
		{
			int tmp = a % b;
			a = b;
			b = tmp;
		}
		out[i] = mult / b;
		
	}

	for (int i = 0; i < T; i++)
		printf("%d\n", out[i]);
		
	return 0;
}
