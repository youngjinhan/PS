/*
두 수가 주어졌을 때 3가지 중 어떤 관계인지 구하기

입력은 여러 테스트 케이스로 이루어져 있다. 각 테스트 케이스는 10,000이 넘지않는 두 자연수로 이루어져 있다. 
마지막 줄에는 0이 2개 주어진다. 두 수가 같은 경우는 없다.

각 테스트 케이스마다 첫 번째 숫자가 두 번째 숫자의 약수라면 factor를, 배수라면 multiple을, 둘 다 아니라면 neither를 출력한다.


ex.
input
8 16
32 4
17 5
0 0

output
factor
multiple
neither

*/

#include <stdio.h>

int main()
{
	int num[10001][2];
	
	for (int i = 0; i < 10000; i++)
	{
		scanf("%d %d", &num[i][0], &num[i][1]);
		if (num[i][0] == 0 && num[i][1] == 0)
			break;
	}
		
	for (int i = 0; i < 10000; i++)
	{
		if (num[i][0] == 0 && num[i][1] == 0)
			break;
		else
		{
			if (num[i][0] < num[i][1])
			{
				if (num[i][1] % num[i][0] == 0)
					printf("factor\n");
				else
					printf("neither\n");
			}

			else
			{
				if (num[i][0] % num[i][1] == 0)
					printf("multiple\n");
				else
					printf("neither\n");
			}
		}
	}
	
		
	
	return 0;
}
