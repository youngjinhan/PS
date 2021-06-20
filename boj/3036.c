/*
첫째 줄에 링의 개수 N이 주어진다. (3 ≤ N ≤ 100)
다음 줄에는 링의 반지름이 순서대로 주어진다. 반지름은 1과 1000를 포함하는 사이의 자연수이다.
출력은 총 N-1줄을 해야 한다. 첫 번째 링을 제외한 각각의 링에 대해서, 첫 번째 링을 한 바퀴 돌리면 그 링은 몇 바퀴 도는지 기약 분수 형태 A/B로 출력한다.

ex.
input
4
12 3 8 4

output
4/1
3/2
3/1
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
	int ring[100], N;
	scanf("%d", &N);
	for (int i = 0; i < N; i++)
		scanf("%d", &ring[i]);

	for (int i = 1; i < N; i++)
		printf("%d/%d\n", ring[0] / gcd(ring[0], ring[i]), ring[i] / gcd(ring[0], ring[i]));
	
	return 0;
}
