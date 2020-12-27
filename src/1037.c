/*
양수 A가 N의 진짜 약수가 되려면, N이 A의 배수이고, A가 1과 N이 아니어야 한다. 
어떤 수 N의 진짜 약수가 모두 주어질 때, N을 구하는 프로그램을 작성하시오.
첫째 줄에 N의 진짜 약수의 개수가 주어진다. 이 개수는 50보다 작거나 같은 자연수이다. 둘째 줄에는 N의 진짜 약수가 주어진다. 
1,000,000보다 작거나 같고, 2보다 크거나 같은 자연수이고, 중복되지 않는다.
첫째 줄에 N을 출력한다. N은 항상 32비트 부호있는 정수로 표현할 수 있다.

@@해결 포인트@@
약수들 중 가장 작은 수와 가장 큰 수를 곱하면 N이다.

ex.
input
2
4 2

output
8

*/


#include <stdio.h>

int main()
{
	int div[50], num, min, max;
	scanf("%d", &num);
	for (int i = 0; i < num; i++)
		scanf("%d", &div[i]);

	min = max = div[0];
	for (int i = 1; i < num; i++)
	{
		if (div[i] > max)
			max = div[i];
		else if (div[i] < min)
			min = div[i];
	}

	printf("%d", min * max);
	
	return 0;
}
