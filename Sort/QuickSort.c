#include <stdio.h>

int size, i = 0;

int partition(int a[], int begin, int end)
{
	int pivot, temp, L, R, t;
	L = begin;
	R = end;
	pivot = (begin + end) / 2;
	printf("\n [ %d 단계 : pivot=%d] \n", ++i, a[pivot]);
	while (L < R) {
		while ((a[L] < a[pivot]) && (L < R))
			L++;
		while ((a[R] >= a[pivot]) && (L < R))
			R--;
		if (L < R) {
			temp = a[L];
			a[L] = a[R];
			a[R] = temp;
		}
	}
	temp = a[pivot];
	a[pivot] = a[R];
	a[R] = temp;

	for (t = 0; t < size; t++)
		printf(" %d", a[t]);
	printf("\n");
	return L;
}

void quickSort(int a[], int begin, int end)
{
	if (begin < end) {
		int p;
		p = partition(a, begin, end); // p에 L(위치가 확정된 pivot)의 인덱스를 저장 
		//printf("%d %d %d\n", p, begin, end);
		quickSort(a, begin, p - 1); // 왼쪽 부분집합
		quickSort(a, p + 1, end);	// 오른쪽 부분집합
	}
}

void main()
{
	int list[8] = { 69,10,30,2,16,8,31,22 };
	size = 8;

	quickSort(list, 0, size - 1);
	getchar();
}