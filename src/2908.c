/*
두 수 A와 B가 주어졌을 때, 각각의 숫자를 거꾸로 재구성하여 나온 두 수를 비교하여 더 큰 값을 출력. 
A와 B는 같지 않은 세 자리 수이며, 0이 포함되어 있지 않다.

ex.
input
734 893

output
437
*/

#include <stdio.h>

int result=0;
void swap(int a)
{
	int tmp = a / 100;
	a = (a % 10) * 100 + ((a / 10) % 10) * 10 + tmp;
	if (a > result)
		result = a;
}
int main()
{
	int n, m;
	scanf("%d %d", &n, &m);
	swap(n);
	swap(m);
	printf("%d", result);

	
	

	return 0;

}
