/*
첫째 줄에 수의 개수 N(2 ≤ N ≤ 11)가 주어진다. 둘째 줄에는 A1, A2, ..., AN이 주어진다. (1 ≤ Ai ≤ 100) 
셋째 줄에는 합이 N-1인 4개의 정수가 주어지는데, 차례대로 덧셈(+)의 개수, 뺄셈(-)의 개수, 곱셈(×)의 개수, 나눗셈(÷)의 개수이다. 
첫째 줄에 만들 수 있는 식의 결과의 최댓값을, 둘째 줄에는 최솟값을 출력한다. 연산자를 어떻게 끼워넣어도 항상 -10억보다 크거나 같고, 10억보다 작거나 같은 결과가 나오는 입력만 주어진다. 
또한, 앞에서부터 계산했을 때, 중간에 계산되는 식의 결과도 항상 -10억보다 크거나 같고, 10억보다 작거나 같다.

ex1.
input
2
5 6
0 0 1 0

output
30
30

ex2.
input
3
3 4 5
1 0 1 0

output
35
17

ex3.
input
6
1 2 3 4 5 6
2 1 1 1

output
54
-24
*/

#include <stdio.h>

int num[12], oper[5];
int N, sum, max=-1000000000, min=1000000000, count = 0;

void sol(int a)
{
	
	if (count == N-1)
	{
		if (sum > max)
			max = sum;
		if (sum < min)
			min = sum;
		

	}

	if (oper[0] == 0 && oper[1] == 0 && oper[2] == 0 && oper[3] == 0)
		return;

	for (int i = 0; i < 4; i++)
	{
		if (i == 0)  // 덧셈
		{
			sum = num[a] + num[a + 1];
			if (oper[i] > 0)  // 연산 가능 (사용하지 않은 덧셈 기호 남아 있을 때)
			{
				oper[i]--;
				int tmp = num[a + 1];
				num[a + 1] = sum;
				count++;
				sol(a + 1);
				count--;
				oper[i]++;
				num[a + 1] = tmp;
			}

			else // 연산 불가 (더 이상 해당 연산 기호 남아있지 않음)
			{
				continue;
			}
		}
			
		else if (i == 1)
		{
			sum = num[a] - num[a + 1];
			
			if (oper[i] > 0)  // 연산 가능 (사용하지 않은 덧셈 기호 남아 있을 때)
			{
				oper[i]--;
				int tmp = num[a + 1];
				num[a + 1] = sum;
				count++;
				sol(a + 1);
				count--;
				oper[i]++;
				num[a + 1] = tmp;
			}

			else // 연산 불가 (더 이상 해당 연산 기호 남아있지 않음)
			{

				continue;
			}
		}
			
		else if (i == 2)
		{
			sum = num[a] * num[a + 1];
			if (oper[i] > 0)  // 연산 가능 (사용하지 않은 덧셈 기호 남아 있을 때)
			{
				oper[i]--;
				int tmp = num[a + 1];
				num[a + 1] = sum;
				count++;
				sol(a + 1);
				count--;
				oper[i]++;
				num[a + 1] = tmp;
			}

			else // 연산 불가 (더 이상 해당 연산 기호 남아있지 않음)
			{
				continue;
			}
		}
			
		else
		{
			sum = num[a] / num[a + 1];
			if (oper[i] > 0)  // 연산 가능 (사용하지 않은 덧셈 기호 남아 있을 때)
			{
				oper[i]--;
				int tmp = num[a + 1];
				num[a + 1] = sum;
				count++;
				sol(a + 1);
				count--;
				oper[i]++;
				num[a + 1] = tmp;
			}

			else // 연산 불가 (더 이상 해당 연산 기호 남아있지 않음)
			{
				continue;
			}
		}
			
	}

	
	

}

int main()
{
	
	scanf("%d", &N);
	for (int i = 0; i < N; i++)
		scanf("%d", &num[i]);
	for (int i = 0; i < 4; i++)
		scanf(" %d", &oper[i]);
		
	sol(0);
	printf("%d\n%d\n", max, min);
	return 0;

}


