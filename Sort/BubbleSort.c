#include <stdio.h>

typedef int element;
int size;

void bubbleSort(int a[], int size)
{
	int i, j, t, cnt = 1;
	element temp;
	printf("\n정렬할 원소 :");
	for (t = 0; t < size; t++)
		printf("%d ", a[t]);
	printf("\n\n<<<<<<<<<<<<< 버블 정렬 수행 >>>>>>>>>>>>>\n");
	for (i = size - 1; i >= 0; i--)
	{
		if (i > 0)
			printf("%d단계>>\n", cnt++);
		for (j = 1; j <= i; j++)
		{
			if (a[j - 1] > a[j])
			{
				temp = a[j - 1];
				a[j - 1] = a[j];
				a[j] = temp;
			}
			printf("\t");
			for (t = 0; t < size; t++)
				printf("%3d", a[t]);
			printf("\n");
		}
	}
}

void main()
{
	element list[10] = { 69,70,10,54,30,2,16,8,31,22 };
	size = 10;
	bubbleSort(list, size);
	getchar();
}