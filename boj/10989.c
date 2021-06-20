// N개의 수가 주어졌을때 오름차순으로 정리하기

/*
첫째 줄에 수의 개수 N(1 ≤ N ≤ 10,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 숫자가 주어진다. 이 수는 10,000보다 작거나 같은 자연수이다.
첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.

N의 개수가 무척 크므로 nlogn의 복잡도를 가진 정렬로도 메모리 초과가 남 -> 카운팅 정렬 사용

ex.
input
10
5
2
3
1
4
2
3
5
1
7

output
1
1
2
2
3
3
4
5
5
7
*/


#include <stdio.h>


int Count[10001];
int max=0;


int main() {
	int N, i, tmp;
	scanf("%d", &N);

	for (i = 0; i < N; i++)
	{
		scanf("%d", &tmp);
		if (max < tmp) max = tmp;
		Count[tmp]++;
	}

	for (int i = 1; i <= max; i++)
	{

		
		while (Count[i]-- != 0)
		{
			printf("%d\n", i);
		}
			
	}


	return 0;
}
